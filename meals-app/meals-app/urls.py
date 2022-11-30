from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="meals/", permanent=True)),
    path("admin/", admin.site.urls),
    path("meals/", include("meals.urls")),
    path("", include("django.contrib.auth.urls")),
]
