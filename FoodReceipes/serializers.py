from rest_framework import serializers
from .models import FoodRecipe

class FoodRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipe
        fields = '__all__'

    def validate_name(self, value):
        if self.instance:
            if FoodRecipe.objects.filter(name=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("This recipe name already exists.")
        else:
            if FoodRecipe.objects.filter(name=value).exists():
                raise serializers.ValidationError("This recipe name already exists.")
        return value

    def validate(self, data):
        for field in ['name', 'description', 'ingredients', 'method', 'category']:
            if not data.get(field):
                raise serializers.ValidationError({field: "This field cannot be blank."})
        return data
    
    def validate_Data_type(self, data):
        if 'name' in data and not isinstance(data['name'], str):
            raise serializers.ValidationError({"name": "The name must be a string."})
        if 'description' in data and not isinstance(data['description'], str):
            raise serializers.ValidationError({"description": "The description must be a string."})
        if 'ingredients' in data and not isinstance(data['ingredients'], str):
            raise serializers.ValidationError({"ingredients": "The ingredients must be a string."})
        if 'method' in data and not isinstance(data['method'], str):
            raise serializers.ValidationError({"method": "The method must be a string."})
        if 'category' in data and not isinstance(data['category'], str):
            raise serializers.ValidationError({"category": "The category must be a string."})
        if 'type' in data and data['type'] not in [FoodRecipe.VEG, FoodRecipe.NON_VEG]:
            raise serializers.ValidationError({"type": "The type must be 'VEG' or 'NON-VEG'."})
        return data