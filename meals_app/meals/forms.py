from django import forms
from meals.models import Meal


class DateInput(forms.DateInput):
    input_type = "date"
    width = "400pt"


class FormForDate(forms.Form):
    date = forms.DateField(widget=DateInput())


not_picked = ("", "-")

class DayForm(forms.Form):
    date = forms.DateField(widget=forms.HiddenInput())
    LU = forms.ChoiceField(
        required=False,
        choices=(not_picked, (Meal.LUNCH, next(x[1] for x in Meal.MEAL_TYPE if x[0] == Meal.LUNCH))),
        widget=forms.Select(attrs={"onchange": "submit()"}),
    )
    DI = forms.ChoiceField(
        required=False,
        choices=(not_picked, (Meal.DINNER, next(x[1] for x in Meal.MEAL_TYPE if x[0] == Meal.DINNER))),
        widget=forms.Select(attrs={"onchange": "submit()"}),
    )

    @staticmethod
    def pupulated_form(day, user):
        meal = DayForm(Meal.meals(day, user))
        return meal


