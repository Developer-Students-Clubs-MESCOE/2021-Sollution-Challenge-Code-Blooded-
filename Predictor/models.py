from django.db import models
import uuid

# Create your models here.
class Predictions(models.Model):
    date = models.CharField(max_length=64, primary_key=True)
    day = models.CharField(max_length=32)
    prediction = models.IntegerField()


class Food_Item(models.Model):
    item_name = models.CharField(max_length=64, unique=True, default=uuid.uuid1)

    def __str__(self):
        return f"{self.item_name}"

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=64, unique=True, default=uuid.uuid1)
    ingredient_unit = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.ingredient_name} {self.ingredient_unit}"

class Recipe(models.Model):
    food = models.ForeignKey(Food_Item, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.food.item_name} {self.ingredient.ingredient_name} {self.quantity}"



