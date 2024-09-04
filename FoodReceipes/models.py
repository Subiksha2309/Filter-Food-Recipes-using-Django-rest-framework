from django.db import models

class FoodRecipe(models.Model):
    VEG = 'VEG'
    NON_VEG = 'NON-VEG'
    RECIPE_TYPE_CHOICES = [
        (VEG, 'Vegetarian'),
        (NON_VEG, 'Non-Vegetarian'),
    ]
    
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=RECIPE_TYPE_CHOICES, default='VEG')

    def __str__(self):
        return self.name
