from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta


class Meal(models.Model):
    BREAKFAST = "BR"
    LUNCH = "LU"
    DINNER = "DI"
    MEAL_TYPE = [
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch"),
        (DINNER, "Dinner"),
    ]

    day = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(
        max_length=2,
        choices=MEAL_TYPE,
        default=BREAKFAST,
    )

    @staticmethod
    def exists(a_day, a_user_id, a_meal):
        if a_user_id is None:
            return False
        a_user = User.objects.get(id=a_user_id)
        day_meals = Meal.objects.filter(day=a_day)
        day_breakfasts = day_meals.filter(meal_type=a_meal)
        day_user_breakfasts = day_breakfasts.filter(user=a_user)
        return day_user_breakfasts.exists()

    @staticmethod
    def meals(a_day, user):
        return {
                "date": a_day,
                Meal.BREAKFAST: Meal.BREAKFAST
                if Meal.exists(a_day, user, Meal.BREAKFAST)
                else "",
                Meal.LUNCH: Meal.LUNCH
                if Meal.exists(a_day, user, Meal.LUNCH)
                else "",
                Meal.DINNER: Meal.DINNER
                if Meal.exists(a_day, user, Meal.DINNER)
                else "",
            }

    class Meta:
        constraints = [models.constraints.UniqueConstraint(
            fields=["day", "user", "meal_type"], name="one_meal_per_person"
        )]

    def meal_description(self):
        return next((x[1] for x in self.MEAL_TYPE if self.meal_type == x[0]))

    def __str__(self):
        return (
            self.day.strftime("%Y-%m-%d")
            + " - "
            + self.user.first_name
            + " "
            + self.user.last_name
            + " - "
            + self.meal_description()
        )

class WeekModel:
    
    @staticmethod
    def days_of_week(a_day):
        weekday = a_day.isoweekday()
        start_of_week = a_day - timedelta(days=weekday)
        return [start_of_week + timedelta(days=d) for d in range(7)]

    def __init__(self, a_day, a_user):
        days = self.days_of_week(a_day)
        self.dict = {every_day : Meal.meals(a_day, a_user) for every_day in days}


