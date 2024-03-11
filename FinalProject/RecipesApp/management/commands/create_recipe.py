from django.core.management.base import BaseCommand
from RecipesApp.models import Recipe
import datetime


class Command_create_recipe(BaseCommand):
    def handle(self, name, desc, steps, time_minutes, author):
        recipe = Recipe(name=name, desc=desc, steps=steps, time_minutes=time_minutes, author=author)
        recipe.save()
        self.stdout.write(f'{recipe}')