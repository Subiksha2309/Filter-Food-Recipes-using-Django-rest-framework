from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FoodRecipe
from .serializers import FoodRecipeSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError


class FoodRecipeCreate(APIView):
    def post(self, request):
        serializer = FoodRecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodRecipeList(generics.ListAPIView):
    serializer_class = FoodRecipeSerializer

    def get_queryset(self):
        queryset = FoodRecipe.objects.all()
        recipe_type = self.request.query_params.get('type')

        if recipe_type:
            if recipe_type not in [FoodRecipe.VEG, FoodRecipe.NON_VEG]:
                raise ValidationError({"type": "Invalid recipe type. Must be 'VEG' or 'NON-VEG'."})
            queryset = queryset.filter(type=recipe_type)

        return queryset
    
class FoodRecipeUpdate(generics.UpdateAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer
    http_method_names = ['patch']    