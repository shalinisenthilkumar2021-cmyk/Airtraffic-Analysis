import requests


def get_flights():
    """
    Fetches live flight data from an external API.
    Returns an empty list gracefully if the API is not configured
    or unreachable, instead of crashing the view.
    """
    url = "YOUR_API_URL"

    if url == "YOUR_API_URL":
        # No real API configured yet — return safe placeholder data
        return []

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return []
