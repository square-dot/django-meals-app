from django.urls import include, path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("user_detail/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
    path("week_view/", views.WeekView.as_view(), name="week_view"),
    path("", RedirectView.as_view(url="day_meals/", permanent=True)),
    path("list_of_users/", views.list_of_users, name="list_of_users"),
    path("login/", views.Login.as_view(), name="login"),
    path("date_picker/", views.CalendarView.as_view(), name="date_picker"),
    path("meal_list/", views.MealsListView.as_view(), name="meals"),
    path("day_meals/", views.DayMeals.as_view(), name="day_meals"),
]
