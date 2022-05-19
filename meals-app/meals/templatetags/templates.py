from django import template
from meals.models import Meal

register = template.Library()


@register.filter(name="pick_meal")
def pick_meal(day, user, meal_type):
    Meal.objects.create(day=day, user=user, meal_type=meal_type)