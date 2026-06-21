from pathlib import Path
from reportlab.pdfgen import canvas
from airtraffic_analysis.settings import BASE_DIR


def create_report():
    """
    Generates a simple PDF report inside MEDIA_ROOT/report.pdf
    and returns the path to the generated file.
    """
    media_dir = BASE_DIR / "media"
    media_dir.mkdir(parents=True, exist_ok=True)

    report_path = media_dir / "report.pdf"

    c = canvas.Canvas(str(report_path))
    c.drawString(100, 750, "Air Traffic Analysis Report")
    c.drawString(100, 730, "Generated automatically by the platform.")
    c.save()

    return report_path
