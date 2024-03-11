from django.shortcuts import render
import logging
from .forms import RecipeForm
from .models import Recipe, Category
from .management.commands.get_1recipe import Command_get_1random_recipe
from .management.commands.create_category import Command_create_category
from .management.commands.create_recipe import Command_create_recipe
from .management.commands.create_recipe_category import Command_create_category_recipe
from django.http import HttpResponse
from random import choice, randint
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page was requested.')
    return render(request, "index.html")

def create_categories(request):
    logger.info('Page of creating categories was requested.')
    names = ['Быстрые', 'Недорогие', 'На праздник']
    for i in names:
        name = i
        desc = f'Описание категории {name}'
        command = Command_create_category()
        command.handle(name, desc)
    return HttpResponse('Категории были созданы')

def create_recipes(request):
    logger.info('Page of creating recipes was requested.')
    names = ['Паста Болоньезе', 'Творожная запеканка', 'Картофельное пюре', 'Куриные котлеты', 'Рисовая каша', 'Бисквитный торт', 'Борщ']
    authors = ['Андрей', 'Аннна', 'Роман', 'Светлана']
    for _ in range(10):
        name = choice(names)
        desc = f'Описание рецепта для {name}'
        time_minutes = randint(10, 50)
        steps = f'Шаги приготовления блюда {name} ...'
        author = choice(authors)
        command = Command_create_recipe()
        command.handle(name, desc, steps, time_minutes, author)
    return HttpResponse('Десять рецептов было создано')

def index_main(request):
    logger.info('Index page with 5 recipes was requested.')
    context = dict()
    command = Command_get_1random_recipe()
    taken = []
    random_recipes = []
    for i in range(5):
        id = randint(1,10)
        while id in taken:
            id = randint(1,10)
        taken.append(id)
        recipe = command.handle(id)
        recipe_text = f'Рецепт приготовления {recipe.name}, время приготовления - {recipe.time_minutes} минут'
        random_recipes.append(recipe_text)
    context['random_recipes_5'] = random_recipes
    return render(request, "index_main.html", context=context)

def index_one_recipe(request):
    logger.info('Index page with 5 recipes was requested.')
    context = dict()
    command = Command_get_1random_recipe()
    id = randint(1,10)
    recipe = command.handle(id)
    context['recipe_name'] = recipe.name
    context['recipe_desc'] = recipe.desc
    context['recipe_steps'] = recipe.steps
    context['recipe_time'] = recipe.time_minutes
    context['recipe_author'] = recipe.author
    return render(request, "index_one_recipe.html", context=context)


def index_edit_recipe(request):
    logger.info('Page with creating recipe was requested.')
    if request.method == 'POST':
        form = RecipeForm(data=request.POST, files=request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            steps = form.cleaned_data['steps']
            time_minutes = form.cleaned_data['time_minutes']
            photo = form.cleaned_data['photo']
            author = form.cleaned_data['author']
            logger.info(f'Получили {name=}, {desc=}, {time_minutes=}, {author=}.')
            recipe = Recipe(name=name, desc=desc, steps = steps, time_minutes=time_minutes, photo = photo, author=author)
            recipe.save()
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
            message = 'Рецепт сохранён'
    else:
        form = RecipeForm()
        message = 'Заполните форму'
    return render(request, 'index_edit_recipe.html', {'form': form, 'message': message})

def index_login(request):
    logger.info('Login/Signup page was requested.')
    return render(request, 'index_login.html')