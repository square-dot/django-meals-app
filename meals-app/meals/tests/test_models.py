from django.test import TestCase
from datetime import date

from django.contrib.auth.models import User
from meals.models import Meal


class MealModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(first_name="Louis", last_name="Pasteur")
        Meal.objects.create(day = date(year=2022, month=9, day=11), user = user, meal_type = "LU")

    def test_setup(self):
        self.assertTrue(User.objects.all().count() == 1)
        self.assertTrue(Meal.objects.filter(meal_type = "LU").count() == 1)
        self.assertTrue(Meal.objects.get(meal_type = "LU").meal_description() == "Lunch")
