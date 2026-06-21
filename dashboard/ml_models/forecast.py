import pandas as pd
from airtraffic_analysis.settings import BASE_DIR

DATA_PATH = BASE_DIR / "data" / "flights.csv"


def run_forecast():
    """
    Lightweight passenger forecast.
    Returns a DataFrame with a 'yhat' column (predicted passengers).
    """
    df = pd.read_csv(DATA_PATH)

    result = pd.DataFrame({
        "yhat": [df["Passengers"].mean()]
    })

    return result
