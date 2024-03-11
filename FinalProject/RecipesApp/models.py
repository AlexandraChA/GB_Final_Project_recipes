from django.db import models

class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    desc =  models.TextField()
    steps =  models.TextField()
    time_minutes = models.IntegerField()
    photo = models.ImageField(upload_to='media/',blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'Recipe: {self.name}, description: {self.desc}, steps: {self.steps}, time to cook: {self.time_minutes}, author: {self.author}'

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return f'Recipe category: {self.name}, description: {self.desc}'
    
class CategoryRecipe(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe_id = models.ForeignKey('Recipe', db_column='recipe_id', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', db_column='category_id', on_delete=models.CASCADE)

    def __str__(self):
        return f'Recipe ID: {self.recipe_id}, Category ID: {self.category_id}'
