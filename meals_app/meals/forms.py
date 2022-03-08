from turtle import width
from django import forms
from meals.models import Commensal
from datetime import date


class DateInput(forms.DateInput):
    input_type = "date"
    width = '400pt'


class MealForm(forms.Form):
    date_field = forms.DateField(widget=DateInput)
    is_at_breakfast = forms.BooleanField(initial=True)
    is_at_lunch = forms.BooleanField(initial=False)
    is_at_dinner = forms.BooleanField(initial=True)

