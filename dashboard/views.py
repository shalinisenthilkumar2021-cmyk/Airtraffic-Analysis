import logging

from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from django.contrib.auth.decorators import login_required

import pandas as pd
import folium
import joblib

from .forms import UploadFileForm
from .report_generator import create_report
from .api_service import get_flights
from .recommendation import get_recommendation
from airtraffic_analysis.settings import BASE_DIR

logger = logging.getLogger('dashboard')

DATA_PATH = BASE_DIR / "data" / "flights.csv"

try:
    from dashboard.ml_models.forecast import run_forecast
except Exception:
    run_forecast = None


def _load_flights():
    """Centralised, safe CSV loader so every view fails the same way."""
    return pd.read_csv(DATA_PATH)


def analytics(request):
    df = _load_flights()

    airports = (
        df.groupby("Destination")["Passengers"]
        .sum()
        .sort_values(ascending=False)
    )

    total_passengers = int(airports.sum())
    busiest_airport = airports.idxmax()

    context = {
        "airports": list(airports.items()),
        "total_passengers": total_passengers,
        "busiest_airport": busiest_airport,
    }

    return render(request, "dashboard/analytics.html", context)


def routes(request):
    df = _load_flights()

    if "Origin" not in df.columns:
        route_data = pd.DataFrame(columns=["Origin", "Destination", "Flights"])
    else:
        route_data = (
            df.groupby(["Origin", "Destination"])
            .size()
            .reset_index(name="Flights")
        )

    return render(request, "dashboard/routes.html", {"routes": route_data.values})


def heatmap(request):
    return render(request, "dashboard/heatmap.html")


@login_required
def upload_file(request):
    success = False

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            success = True
            logger.info(f"User '{request.user}' uploaded file: {instance.file.name}")
            form = UploadFileForm()  # reset form after successful upload
    else:
        form = UploadFileForm()

    return render(request, "dashboard/upload.html", {"form": form, "success": success})


def reports(request):
    create_report()
    return render(request, "dashboard/reports.html")


def ranking(request):
    df = _load_flights()

    airport_rank = (
        df.groupby("Destination")["Passengers"]
        .sum()
        .sort_values(ascending=False)
    )

    return render(request, "dashboard/ranking.html", {"ranking": airport_rank.items()})


def live_flights(request):
    data = get_flights()
    return render(request, "dashboard/live.html", {"data": data})


def recommendations(request):
    recs = get_recommendation()
    return render(request, "dashboard/recommendations.html", {"recs": recs})


def prediction(request):
    delay = None
    error = None

    try:
        model_path = BASE_DIR / "dashboard" / "ml_models" / "delay_model.pkl"
        model = joblib.load(model_path)
        delay = round(float(model.predict([[100]])[0]), 2)
    except FileNotFoundError:
        error = "Delay prediction model not found. Please train the model first."
    except Exception:
        error = "Unable to generate a delay prediction right now."

    return render(request, "dashboard/prediction.html", {"delay": delay, "error": error})


def map_view(request):
    m = folium.Map(location=[22, 78], zoom_start=5)

    airports = [
        ("Chennai", 13.08, 80.27),
        ("Delhi", 28.61, 77.20),
        ("Mumbai", 19.07, 72.87),
        ("Bangalore", 12.97, 77.59),
    ]

    for name, lat, lon in airports:
        folium.Marker([lat, lon], popup=name).add_to(m)

    return render(request, "dashboard/map.html", {"map": m._repr_html_()})


def data_quality(request):
    df = _load_flights()

    duplicates = df.duplicated().sum()
    quality_score = round(((len(df) - duplicates) / len(df)) * 100, 2) if len(df) else 0

    return render(request, "dashboard/data_quality.html", {"quality_score": quality_score})


def airport_score_ranking(request):
    df = _load_flights()

    df["Score"] = (df["Passengers"] * 0.7) + ((100 - df["Delay_Minutes"]) * 0.3)

    ranking_data = df.sort_values(by="Score", ascending=False)

    return render(
        request,
        "dashboard/airport_score.html",
        {"ranking": ranking_data.to_dict("records")},
    )


@login_required
def safety_incidents(request):
    incidents_path = BASE_DIR / "data" / "incidents.csv"

    try:
        df = pd.read_csv(incidents_path)
    except FileNotFoundError:
        return render(request, "dashboard/safety_incidents.html", {"missing": True})

    severity_counts = df["Severity"].value_counts()
    type_counts = df["Incident_Type"].value_counts()
    airport_counts = df["Airport"].value_counts()

    context = {
        "missing": False,
        "incidents": df.to_dict("records"),
        "total_incidents": len(df),
        "most_common_type": type_counts.idxmax(),
        "most_affected_airport": airport_counts.idxmax(),
        "severity_breakdown": severity_counts.items(),
    }

    return render(request, "dashboard/safety_incidents.html", context)


@login_required
def delay_reasons(request):
    df = _load_flights()

    if "Delay_Reason" not in df.columns:
        return render(request, "dashboard/delay_reasons.html", {"reasons": [], "missing": True})

    reason_counts = df["Delay_Reason"].value_counts()
    total = reason_counts.sum()

    reason_data = [
        (reason, count, round((count / total) * 100, 1))
        for reason, count in reason_counts.items()
    ]

    avg_delay_by_reason = df.groupby("Delay_Reason")["Delay_Minutes"].mean().round(1)

    top_reason = reason_counts.idxmax()

    context = {
        "reasons": reason_data,
        "avg_delay_by_reason": avg_delay_by_reason.items(),
        "top_reason": top_reason,
        "missing": False,
    }

    return render(request, "dashboard/delay_reasons.html", context)


@login_required
def dashboard(request):
    df = _load_flights()

    total_passengers = int(df["Passengers"].sum())
    total_flights = len(df)
    avg_delay = df["Delay_Minutes"].mean()

    if avg_delay > 25:
        recommendation = "Increase airport staff"
    elif total_passengers > 4000:
        recommendation = "Open additional boarding gates"
    else:
        recommendation = "Operations running normally"

    top_airport = df.groupby("Destination")["Passengers"].sum().idxmax()

    top3 = (
        df.groupby("Destination")["Passengers"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )

    context = {
        "total_passengers": total_passengers,
        "total_flights": total_flights,
        "avg_delay": round(avg_delay, 2),
        "top_airport": top_airport,
        "recommendation": recommendation,
        "context_top3": top3.items(),
    }

    return render(request, "dashboard/index.html", context)


@login_required
def download_pdf(request):
    create_report()
    report_path = BASE_DIR / "media" / "report.pdf"

    if not report_path.exists():
        logger.error("Report PDF generation failed — file not found.")
        raise Http404("Report not found.")

    logger.info(f"User '{request.user}' downloaded the PDF report.")
    return FileResponse(
        open(report_path, "rb"),
        as_attachment=True,
        filename="air_traffic_report.pdf",
    )


def forecast(request):
    if run_forecast is None:
        return render(request, "dashboard/forecast.html", {"prediction": None})

    forecast_data = run_forecast()
    prediction = forecast_data["yhat"].tail(1).values[0]

    return render(request, "dashboard/forecast.html", {"prediction": round(prediction, 2)})
