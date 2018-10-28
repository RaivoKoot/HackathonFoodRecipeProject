from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.template import loader
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


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
    return render(request, 'pages/inventory.html')
