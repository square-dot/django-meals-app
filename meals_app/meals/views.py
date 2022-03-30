from django.shortcuts import render
from meals.models import Meal
from datetime import date
from .forms import FormForDate, FormForDate, MealForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.core.exceptions import ValidationError


class Week_view(View, LoginRequiredMixin):
    template_name = "week_view.html"

    def get(self, request):
        meals_form = self.pupulated_meal_form(date.today(), request.user.id)
        print(meals_form["date"].value())
        return render(request, self.template_name, {"meals_form": meals_form})

    def post(self, request):
        a_date = date.today()
        if "date_change" in request.POST:
            meals_form = MealForm(request.POST)
            if meals_form.is_valid():
                a_date = meals_form["date"].value()
        if "date_change" not in request.POST:
            meals_form = MealForm(request.POST)
            if meals_form.is_valid():
                a_date = meals_form["date"].value()
                a_user = request.user
                for m in Meal.MEAL_TYPE:
                    in_db = (
                        Meal.objects.filter(day=a_date)
                        .filter(user=a_user)
                        .filter(meal_type=m[0])
                    )
                    if in_db.exists() and not meals_form[m[0]].value():
                        in_db.delete()
                    elif not in_db.exists() and meals_form[m[0]].value():
                        Meal.objects.create(day=a_date, user=a_user, meal_type=m[0])
            else:
                return ValidationError
        meals_form = self.pupulated_meal_form(a_date, request.user.id)
        return render(request, self.template_name, {"meals_form": meals_form})

    def is_at_meal(self, a_day, a_user_id, a_meal):
        if a_user_id is None:
            return False
        a_user = User.objects.get(id=a_user_id)
        day_meals = Meal.objects.filter(day=a_day)
        day_breakfasts = day_meals.filter(meal_type=a_meal)
        day_user_breakfasts = day_breakfasts.filter(user=a_user)
        return day_user_breakfasts.exists()

    def pupulated_meal_form(self, day, user):
        meal = MealForm(
            {
                "date": day,
                Meal.BREAKFAST: Meal.BREAKFAST
                if self.is_at_meal(day, user, Meal.BREAKFAST)
                else "",
                Meal.LUNCH: Meal.LUNCH
                if self.is_at_meal(day, user, Meal.LUNCH)
                else "",
                Meal.DINNER: Meal.DINNER
                if self.is_at_meal(day, user, Meal.DINNER)
                else "",
            }
        )
        return meal


class CalendarView(View, LoginRequiredMixin):
    template_name = "date_picker.html"

    def get(self, request):
        date_input = FormForDate(initial={"date": date.today()})
        return render(request, self.template_name, {"date_input": date_input})


def list_of_users(request):
    all_users = {"all_users_list": User.objects.all()}
    template_name = "meals/list_of_users.html"
    return render(request, template_name, all_users)


class Login(LoginView):
    next_page = "login"
    template_name = "login.html"
    next = "week_view.html"


class MealsListView(ListView):
    model = Meal


class DayMeals(View):
    template_name = "day_meals.html"

    def get(self, request):
        day = date.today()
        all_meals = Meal.objects.filter(day=day)
        breakfasts = [x.user for x in all_meals.filter(meal_type=Meal.BREAKFAST)]
        lunches = [x.user for x in all_meals.filter(meal_type=Meal.LUNCH)]
        dinners = [x.user for x in all_meals.filter(meal_type=Meal.DINNER)]

        return render(
            request,
            self.template_name,
            {
                Meal.BREAKFAST: breakfasts,
                Meal.LUNCH: lunches,
                Meal.DINNER: dinners,
            },
        )


class UserDetailView(DetailView):
    model = User
