from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class DashboardViewsTestCase(TestCase):
    """Smoke tests to make sure core pages load without crashing."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='tester', password='testpass123')
        self.client.login(username='tester', password='testpass123')

    def test_dashboard_loads(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_analytics_loads(self):
        response = self.client.get(reverse('analytics'))
        self.assertEqual(response.status_code, 200)

    def test_ranking_loads(self):
        response = self.client.get(reverse('ranking'))
        self.assertEqual(response.status_code, 200)

    def test_data_quality_loads(self):
        response = self.client.get(reverse('data_quality'))
        self.assertEqual(response.status_code, 200)

    def test_recommendations_loads(self):
        response = self.client.get(reverse('recommendations'))
        self.assertEqual(response.status_code, 200)

    def test_prediction_loads_even_without_model(self):
        # Should render gracefully even if the .pkl model is missing
        response = self.client.get(reverse('prediction'))
        self.assertEqual(response.status_code, 200)
