# ✈️ Air Traffic Intelligence Platform

An AI-powered air traffic analytics and forecasting dashboard built with Django.
It analyzes flight passenger data, predicts delays using a trained ML model,
forecasts future passenger demand, and visualizes airport performance on an
interactive map and ranking system.

## Features

- 🔐 **Authentication** — Signup, login, logout (Django auth)
- 📊 **Dashboard** — key metrics: total passengers, total flights, average delay (login required)
- 📈 **Analytics** — passenger volume breakdown by destination airport
- ⏱ **Delay Prediction** — ML model (scikit-learn) predicts flight delay
- 🔮 **Forecasting** — passenger demand forecasting
- 🗺 **Flight Map** — interactive Folium map of major airports
- 🏆 **Airport Ranking** — airports ranked by total passenger volume
- ⭐ **Airport Score** — composite score (passengers + on-time performance)
- ✅ **Data Quality** — automated data quality scoring (duplicates, completeness)
- 📄 **Reports** — generate and download a PDF analytics report
- 🤖 **AI Insights** — automated operational recommendations
- 📤 **Upload Data** — upload new flight datasets via the dashboard (login required)
- 🌐 **REST API** — JSON endpoints for airports, flights, uploads, and summary stats (Django REST Framework)
- 📝 **Logging** — request/event logging to console and `logs/app.log`
- ⚙️ **Environment-based config** — secrets and settings via `.env` (python-decouple)

## Tech Stack

- **Backend:** Django 5, Django REST Framework
- **Auth:** Django built-in authentication
- **Config:** python-decouple (.env)
- **Data processing:** pandas, NumPy
- **Machine Learning:** scikit-learn, Prophet
- **Visualization:** Plotly, Folium
- **PDF generation:** ReportLab
- **Database:** SQLite (dev)

## REST API Endpoints

| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/api/summary/` | GET | Public | Aggregate flight stats (total flights, passengers, avg delay) |
| `/api/airports/` | GET, POST | Read: public, Write: login | List / create airports |
| `/api/flights/` | GET, POST | Read: public, Write: login | List / create flights |
| `/api/upload/` | GET, POST | Login required | Upload flight data files |

Browsable API available at `/api/` (DRF default UI) — login via `/api-auth/login/`.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Airtraffic-Analysis.git
cd Airtraffic-Analysis
```

### 2. Create a virtual environment & install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the example env file and adjust if needed (default values work out of the box for local dev):

```bash
cp .env.example .env
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Create an account

Sign up via the app at `/signup/`, or create an admin account:

```bash
python manage.py createsuperuser
```

### 6. (Optional) Train the ML models

```bash
python dashboard/train_model.py
python dashboard/train_forecast.py
```

### 7. Start the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

## Project Structure

```
Airtraffic-Analysis/
├── airtraffic_analysis/   # Django project settings & URLs
├── dashboard/             # Main app: views, models, templates, ML models
│   ├── ml_models/         # Trained model files + forecasting logic
│   ├── templates/         # Dashboard HTML templates
│   ├── static/            # CSS / JS
│   ├── views.py
│   └── models.py
├── data/                  # Sample flight datasets (CSV)
├── media/                 # Generated reports & uploaded files (gitignored)
├── requirements.txt
└── manage.py
```

## Roadmap / Future Improvements

- [ ] Replace sample CSV with a live flight-data API
- [ ] Add user authentication & role-based dashboards
- [ ] Switch from SQLite to PostgreSQL for production
- [ ] Add automated tests (pytest / Django TestCase)
- [ ] Deploy to Render / Railway with a live demo link
- [ ] Add CSV/Excel export for all report types

## Author

**Your Name**
- 📄 [Resume](YOUR_RESUME_LINK_HERE)
- 🌐 [Portfolio](YOUR_PORTFOLIO_LINK_HERE)
- 💻 [GitHub](https://github.com/YOUR_GITHUB_USERNAME)
