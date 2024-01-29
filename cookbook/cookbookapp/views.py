from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Product, Recipe, RecipeProduct


def index(request):
    return HttpResponse ("<h1>Hello</h1>")


def add_product_to_recipe(request):
    # Получаем значения параметров из GET-запроса
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')
    
    # Получаем объекты рецепта и продукта по их ID
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    product = get_object_or_404(Product, pk=product_id)

    # Проверяем, существует ли такая связь рецепта и продукта в модели RecipeProduct
    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)

    # Если связь существует, обновляем вес продукта
    if not created:
        recipe_product.weight = weight
        recipe_product.save()
        return JsonResponse({'message': 'Product update to recipe successfully'})
    # Если нет связи, то создаём новую
    else:
        recipe_product.weight = weight
        recipe_product.save()
        return JsonResponse({'message': 'Product added to recipe successfully'})
    