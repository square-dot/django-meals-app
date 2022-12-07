from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from meals.views import list_of_users

app_name = 'meals-app'

urlpatterns = [
    path("", RedirectView.as_view(url="meals/", permanent=True)),
    path("admin/", admin.site.urls),
    path("meals/", include("meals.urls")),
    path("", include("django.contrib.auth.urls")),
    path("administration/list_of_users", list_of_users, name="list_of_users"),
]
