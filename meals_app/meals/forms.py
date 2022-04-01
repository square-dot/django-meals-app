from turtle import width
from django import forms
from datetime import date, timedelta
from meals.models import Meal


class DateInput(forms.DateInput):
    input_type = "date"
    width = "400pt"


class FormForDate(forms.Form):
    date = forms.DateField(widget=DateInput())


not_picked = ("", "-")

class MealForm(forms.Form):
    date = forms.DateField(widget=forms.HiddenInput())
    BR = forms.ChoiceField(
        required=False,
        choices=(not_picked, (Meal.BREAKFAST, next(x[1] for x in Meal.MEAL_TYPE if x[0] == Meal.BREAKFAST))),
        widget=forms.Select(attrs={"onchange": "submit()"}),
    )
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
    def pupulated_meal_form(day, user):
        meal = MealForm(Meal.dictionary_of_day(day, user))
        return meal


