from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/', FoodRecipeCreate.as_view(), name='create-recipe'),
    path('recipes/<int:id>', FoodRecipeList.as_view(), name='list-recipes'),
    path('recipes/<int:pk>/', FoodRecipeUpdate.as_view(), name='update-recipe'),
]
