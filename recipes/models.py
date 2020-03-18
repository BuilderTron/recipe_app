from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# Food Category
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

# Meal Category
class Meal(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)



    class Meta:
        ordering = ('name',)
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name


# Recipe Field
class Recipe(models.Model):

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    daily_meals = (
        ('Breakfast','Breakfast'),
        ('Brunch','Brunch'),
        ('Elevenses','Elevenses'),
        ('Lunch','Lunch'),
        ('Tea','Tea'),
        ('Supper','Supper'),
        ('Dinner','Dinner'),
    )
    # meal = models.CharField(max_length=100, choices = daily_meals)
    meal = models.ForeignKey(Meal, choices = daily_meals, on_delete=models.CASCADE,)
    ingredients = models.TextField(blank=True)
    directions = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
