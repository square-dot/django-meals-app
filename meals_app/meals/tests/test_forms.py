from django.test import TestCase

from meals.forms import DayForm

class SubscribeToMealTest(TestCase):
    def test_pick_meal(self):
        print("Testing empty DayForm is valid")
        form = DayForm()
        self.assertFalse(form.is_valid())