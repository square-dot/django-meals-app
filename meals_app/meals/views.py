from django.shortcuts import render
from meals.models import Commensal, Meal, MealType
from datetime import date
from .forms import MealForm


def calendar(request, user_id):
    if request.method == "POST":
        form = MealForm(request.POST)
        if not form.is_valid():
            form = MealForm()
            current_date = date.today()
        else:
            current_date = form.cleaned_data["date_field"]
            3 / 0
    else:
        form = MealForm()
        current_date = date.today()

    selected = Meal.objects.filter(commensal=Commensal.objects.get(pk=user_id)).filter(
        day=date.today()
    )
    if selected.filter(meal_type=MealType.objects.get(type="breakfast")):
        is_at_breakfast = True
    else:
        is_at_breakfast = False
    if selected.filter(meal_type=MealType.objects.get(type="lunch")):
        is_at_lunch = True
    else:
        is_at_lunch = False
    if selected.filter(meal_type=MealType.objects.get(type="dinner")):
        is_at_dinner = True
    else:
        is_at_dinner = False

    user_and_meals = {
        "meal_form": form,
        "current_date": current_date,
        "current_user": Commensal.objects.get(pk=user_id),
    }
    template_name = "meals/commensal_week_view.html"
    return render(request, template_name, user_and_meals)


def user_page(request, user_id):
    all_users = {"current_user": Commensal.objects.get(pk=user_id)}
    template_name = "meals/user_page.html"
    return render(request, template_name, all_users)


def list_of_users(request):
    all_users = {"all_users_list": Commensal.objects.all()}
    template_name = "meals/list_of_users.html"
    return render(request, template_name, all_users)
