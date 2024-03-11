from django.core.management.base import BaseCommand
from RecipesApp.models import CategoryRecipe
import datetime


class Command_create_category_recipe(BaseCommand):
    def handle(self, recipe_id, category_id):
        categoryrecipe = CategoryRecipe(recipe_id=recipe_id, category_id = category_id)
        categoryrecipe.save()
        self.stdout.write(f'{categoryrecipe}')