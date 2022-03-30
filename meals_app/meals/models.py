from django.db import models
from django.contrib.auth.models import User


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