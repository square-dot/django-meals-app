from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from meals.models import Meal

from datetime import date


class WeekViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(first_name="Louis", last_name="Pasteur")
        Meal.objects.create(day = date(year=2022, month=9, day=11), user = user, meal_type = "LU")

    # def test_view_url_exists_at_desired_location(self):
    #     response = self.client.get('/meals/week_view')
    #     self.assertEqual(response.status_code, 200)

    # def test_view_url_accessible_by_name(self):
    #     response = self.client.get(reverse('week_view'))
    #     self.assertEqual(response.status_code, 200)