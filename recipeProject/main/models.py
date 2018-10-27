from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from accounts.models import Account


class Category(models.Model):
    name = models.CharField(max_length = 200, unique=True)


class Ingredient(models.Model):
    name = models.CharField(max_length = 100, unique=True)


class Recipe(models.Model):
    author = models.ForeignKey(Account, on_delete = models.SET_NULL, null=True)
    title = models.TextField()

    date_published = models.DateTimeField(default=timezone.now())
    rating = models.FloatField(null = True)

    fat = models.FloatField(null = True)
    calories = models.FloatField(null = True)
    protein = models.FloatField(null = True)
    sodium = models.FloatField(null = True)

    categories = models.ManyToManyField(Category, through='RecipeCategory')


class DetailedIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete = models.SET_NULL, null = True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.TextField()


class Direction(models.Model):
    order = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    content = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together=('order', 'recipe')


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Container(models.Model):
    pass
