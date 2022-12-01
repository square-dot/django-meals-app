from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import MealUserCreationForm, MealUserChangeForm
from .models import MealUser

class MealUserAdmin(UserAdmin):
    add_form = MealUserCreationForm
    form = MealUserChangeForm
    model = MealUser
    list_display = ["email", "username",]

admin.site.register(MealUser, MealUserAdmin)
