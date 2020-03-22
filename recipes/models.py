from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# User Profile
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default_user.jpg', upload_to='recipes/users')
#
#     def __str__(self):
#         return f'{self.user.username} Profile'






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


# Default Recipe images
# 
# class Defailt_img(models.Model):
#     image = models.ImageField(default='recipes/default.png',upload_to='recipes/images/', blank=True)


# Recipe Field
class Recipe(models.Model):
    title = models.CharField(max_length=200)
# FIXME: If default image is changed to user's upload but then deleted. Make default image reappear.
    image = models.ImageField(default='recipes/default.png',upload_to='recipes/images/', blank=True)
    url = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    daily_meals = ['Breakfast', 'Brunch', 'Elevenses', 'Lunch', 'Tea', 'Supper', 'Dinner']
    meal = models.ForeignKey(Meal, limit_choices_to={'name__in': daily_meals}, on_delete=models.CASCADE,)

    image_ingredients = models.ImageField(upload_to='recipes/images/', null=False, blank=True)
    ingredients = models.TextField(blank=True)

    image_directions = models.ImageField(upload_to='recipes/images/', blank=True)
    directions = models.TextField(blank=True)
    image_final = models.ImageField(upload_to='recipes/images/', blank=True)
    serving_instructions = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
