from django.core.management.base import BaseCommand
from RecipesApp.models import Category
import datetime


class Command_create_category(BaseCommand):
    def handle(self, name, desc):
        category = Category(name=name, desc = desc)
        category.save()
        self.stdout.write(f'{category}')