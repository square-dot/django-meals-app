from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("user_detail/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
    path("week_view/", views.Week_view.as_view(), name="week_view"),
    path("", RedirectView.as_view(url="week_view/", permanent=True)),
    path("list_of_users/", views.list_of_users, name="list_of_users"),
    path("login/", views.Login.as_view(), name="login"),
    path("change_week/", views.Week_view.as_view(), name="change_week"),
    path("date_picker/", views.CalendarView.as_view(), name="date_picker"),
    path("meal_list/", views.MealsListView.as_view(), name="meals"),
    path("day_meals/", views.DayMeals.as_view(), name="day_meals"),
]