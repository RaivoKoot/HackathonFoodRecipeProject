from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, Inventory, IngredientInventory
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from data_processing import similarity_model


def recipes_index(request):

    latest_recipes = Recipe.objects.order_by('-date_published')[:6]
    context = {'latest_recipes':latest_recipes,}

    return render(request, 'index.html', context)


def recipes_detail(request, id):

    recipe = None

    try:
        recipe = Recipe.objects.get(id = id)
    except:
        return Http404('Recipe not found!')

    context = {'recipe': recipe}

    return render(request, 'pages/recipe.html', context)


def recipes_list(request):

    keyword = request.GET.get('search')
    if keyword is None:
        keyword = ''

    recipe_list = Recipe.objects.filter(title__icontains = keyword)
    paginator = Paginator(recipe_list, 10)

    page = request.GET.get('page')
    if page is not None:
        page = int(page)
    recipes = paginator.get_page(page)
    context = {'recipes': recipes,
                'num_pages': paginator.page_range,
                'current_page': page,
                'search': keyword}

    return render(request, 'pages/recipe_search.html', context)


def inventory(request):
    keyword = request.GET.get('search')
    if keyword is None:
        keyword = ''

    inventory = None
    try:
        inventory = Inventory.objects.get(owner__id = request.user.id)
    except:
        inventory = Inventory(owner = request.user)
        inventory.save()

    new_ingredient_list = Ingredient.objects.filter(name__icontains = keyword)
    paginator = Paginator(new_ingredient_list, 10)

    page = request.GET.get('page')
    if page is not None:
        page = int(page)
    new_ingredients = paginator.get_page(page)
    context = {'ingredients': new_ingredients,
                'num_pages': paginator.page_range,
                'current_page': page,
                'search': keyword,
                'inventory': inventory,}
    return render(request, 'pages/inventory.html', context)


def add_to_inventory(request, id):
    inventory = Inventory.objects.get(owner__id = request.user.id)
    ingredient = Ingredient.objects.get(id = id)

    inv_ingr = IngredientInventory(inventory = inventory, ingredient = ingredient)
    inv_ingr.save()

    return HttpResponseRedirect('/inventory')


def remove_from_inventory(request, id):
    IngredientInventory.objects.filter(inventory__owner__id = request.user.id, ingredient__id = id)[0].delete()
    return HttpResponseRedirect('/inventory')


def get_recipe_recommendations(request):
    inventory = Inventory.objects.get(owner__id = request.user.id)
    matching_recipes = []

    for recipe in Recipe.objects.all():
        matching = True
        if recipe.detailedingredient_set.count() < 1:
            continue
        for recipe_ingredient in recipe.detailedingredient_set.all():
            if recipe_ingredient.ingredient not in inventory.ingredients.all():
                matching = False
                break
        if matching:
            matching_recipes.append(str(recipe.id) + " " + recipe.title + "<br>")

    return HttpResponse(matching_recipes)
