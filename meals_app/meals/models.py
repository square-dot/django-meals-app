from django.db import models
from datetime import datetime

from numpy import empty


class Commensal(models.Model):
    first_name = models.CharField(max_length=200, default="")
    family_name = models.CharField(max_length=200, default="")
    creation_time = models.DateTimeField("creation time")

    def __str__(self):
        return self.first_name + " " + self.family_name

    def fullname(self):
        return self.first_name + " " + self.family_name

    def sign_in_for_meal(self, day, meal_type):
        meal = Meal(commensal=self, day=day, meal_type=meal_type)
        meal.save()

    def cancel_for_meal(self, day, meal_type):
        Meal.objects.filter(commensal=self).filter(day=day).filter(
            meal_type=meal_type
        ).delete()

    def is_in_for_meal(self, day, meal_type):
        return (
            Meal.objects.filter(user=self).filter(day=day).filter(meal_type=meal_type)
            is not empty
        )


class MealType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Meal(models.Model):
    day = models.DateField()
    commensal = models.ForeignKey(Commensal, on_delete=models.CASCADE)
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)

    class Meta:
        models.constraints.UniqueConstraint(
            fields=["day", "commensal", "meal_type"], name="one_meal_per_person"
        )

    def __str__(self):
        return (
            self.day.strftime("%Y-%m-%d")
            + " "
            + self.commensal.fullname()
            + " "
            + self.meal_type.__str__()
        )
