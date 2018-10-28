from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.template import loader
from django.http import Http404

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
