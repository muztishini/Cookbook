from django.urls import path
from .views import index, add_product_to_recipe, cook_recipe,  show_recipes_without_product


urlpatterns = [
    path("", index, name="home"),
    path("add_product_to_recipe/", add_product_to_recipe),
    path("cook_recipe/", cook_recipe),
    path("show_recipes_without_product/",  show_recipes_without_product)
]
