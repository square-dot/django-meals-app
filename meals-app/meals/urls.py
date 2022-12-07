from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", RedirectView.as_view(url="week_view", permanent=True)),
    path("meal_picker", views.MealPicker.as_view(), name="meal_picker"),
    path("date_picker", views.CalendarView.as_view(), name="date_picker"),
    path("list_of_meals", views.MealsListView.as_view(), name="list_of_meals"),
    path("meals_of_the_day", views.MealsOfTheDay.as_view(), name="meals_of_the_day"),
    path("user_detail/<int:pk>", views.UserDetailView.as_view(), name="user_detail"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.Login.as_view(), name="login"),
]
