from unittest import TestCase
from datetime import date

from django.contrib.auth.models import User
from meals.forms import DayForm
from meals.models import Meal


class SubscribeToMealTest(TestCase):

    def setUp(self):
        User.objects.create(username = "lpa", first_name="Louis", last_name="Pasteur")

    def tearDown(self):
        User.objects.all().delete()

    def test_pick_meal(self):
        # Testing empty DayForm is not valid
        form = DayForm()
        self.assertFalse(form.is_valid())

    def test_pick_lunch(self):
        user = User.objects.get()
        chosen_date = date(2022, 1, 1)
        form = DayForm(
            {
                "date": chosen_date,
                "BR": DayForm().not_picked,
                "LU": DayForm().picked_string,
                "DI": DayForm().not_picked,
            }
        )
        form.process(user)
        self.assertTrue(
            Meal.objects.filter(day=chosen_date)
            .filter(user=user)
            .filter(meal_type="LU")
            .exists()
        )