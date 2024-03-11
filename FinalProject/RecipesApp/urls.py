from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('createRecipes/', views.create_recipes, name='create_recipes'),
    path('createCategories/', views.create_categories, name='create_categories'),
    path('main/', views.index_main, name='index_main'),
    path('login/', views.index_login, name='index_login'),
    path('oneRandomRecipe/', views.index_one_recipe, name='index_one_recipe'),
    path('createRecipeManually/', views.index_edit_recipe, name='index_edit_recipe'),
    ]