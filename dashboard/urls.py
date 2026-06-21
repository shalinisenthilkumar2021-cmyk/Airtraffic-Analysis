from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import auth_views as custom_auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('signup/', custom_auth_views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics, name='analytics'),
    path('routes/', views.routes, name='routes'),
    path('forecast/', views.forecast, name='forecast'),
    path('prediction/', views.prediction, name='prediction'),
    path('delay-reasons/', views.delay_reasons, name='delay_reasons'),
    path('safety-incidents/', views.safety_incidents, name='safety_incidents'),
    path('heatmap/', views.heatmap, name='heatmap'),
    path('upload/', views.upload_file, name='upload'),
    path('ranking/', views.ranking, name='ranking'),
    path('live/', views.live_flights, name='live'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('reports/', views.reports, name='reports'),
    path("map/",views.map_view,name="map"),
    path("data-quality/",views.data_quality,name="data_quality"),
    path("airport-score/",views.airport_score_ranking,name="airport_score"),
    path('download-pdf/',views.download_pdf,name='download_pdf'),
    # path("download-report/",views.download_report,name="download_report"),
]
