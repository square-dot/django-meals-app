from django.shortcuts import render
from meals.models import Meal, WeekModel
from datetime import date
from .forms import FormForDate, FormForDate, DayForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.core.exceptions import ValidationError


class WeekView(View, LoginRequiredMixin):
    template_name = "week_view.html"

    def get(self, request):
        days_of_week = WeekModel.days_of_week(date.today())
        monday_form = DayForm.pupulated_form(days_of_week[0], request.user.id)
        tuesday_form = DayForm.pupulated_form(days_of_week[1], request.user.id)
        wednesday_form = DayForm.pupulated_form(days_of_week[2], request.user.id)
        return render(
            request,
            self.template_name,
            {
                "monday_form": monday_form,
                "tuesday_form": tuesday_form,
                "wednesday_form": wednesday_form,
            }
        )

    def post(self, request):
        a_date = date.today()
        if "date_change" in request.POST:
            meals_form = DayForm(request.POST)
            if meals_form.is_valid():
                a_date = meals_form["date"].value()
        if "date_change" not in request.POST:
            print('date change not in request post')
            meals_form = DayForm(request.POST)
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
        days_of_week = WeekModel.days_of_week(date.today())
        monday_form = DayForm.pupulated_form(days_of_week[0], request.user.id)
        tuesday_form = DayForm.pupulated_form(days_of_week[1], request.user.id)
        wednesday_form = DayForm.pupulated_form(days_of_week[2], request.user.id)
        return render(
            request,
            self.template_name,
            {
                "monday_form": monday_form,
                "tuesday_form": tuesday_form,
                "wednesday_form": wednesday_form,
            }
        )


class DayView(View, LoginRequiredMixin):
    template_name = "day_view.html"

    def get(self, request):
        meals_form = DayForm.pupulated_form(date.today(), request.user.id)
        return render(request, self.template_name, {"meals_form": meals_form})

    def post(self, request):
        a_date = date.today()
        if "date_change" in request.POST:
            meals_form = DayForm(request.POST)
            if meals_form.is_valid():
                a_date = meals_form["date"].value()
        if "date_change" not in request.POST:
            meals_form = DayForm(request.POST)
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
        meals_form = DayForm.pupulated_form(a_date, request.user.id)
        return render(request, self.template_name, {"meals_form": meals_form})


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
        lunches = [x.user for x in all_meals.filter(meal_type=Meal.LUNCH)]
        dinners = [x.user for x in all_meals.filter(meal_type=Meal.DINNER)]

        return render(
            request,
            self.template_name,
            {
                Meal.LUNCH: lunches,
                Meal.DINNER: dinners,
            },
        )


class UserDetailView(DetailView):
    model = User
