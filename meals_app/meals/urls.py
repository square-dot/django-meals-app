from django.urls import path
from . import views

urlpatterns = [
    path("user/<int:user_id>/", views.user_page, name="user"),
    path('user/<int:user_id>/calendar', views.calendar, name="calendar"),
    path('users/list/', views.list_of_users, name="list_of_users"),
]
