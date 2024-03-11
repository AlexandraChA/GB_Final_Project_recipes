from django.core.management.base import BaseCommand
from RecipesApp.models import Recipe

class Command_get_1random_recipe(BaseCommand):

    def handle(self, id):
        id = id
        recipe = Recipe.objects.filter(pk=id).first()
        self.stdout.write(f'{recipe}')
        return recipe