from django.core.management.base import BaseCommand
from main.models import *
import pandas as pd
from main.models import Category, Recipe, DetailedIngredient, Ingredient

class Command(BaseCommand):
    # args = '<foo bar ...>'
    # help = 'our help string comes here'

    def handle(self, *args, **options):
        self.feed_ingredients()
        self.feed_data_to_database()


    def feed_ingredients(self):
        ingredients = list(pd.read_csv('../python model/data/ingredient_info.tsv', delimiter='\t')['ingredient name'].values)
        for ingredient_name in ingredients:
            try:
                ingredient = Ingredient.objects.get(name = ingredient_name.replace('_', ' '))
            except:
                ingredient = Ingredient(name = ingredient_name.replace('_', ' '))
                ingredient.save()


    def get_matching_recipes(self):
        recipes = pd.read_json('../data_processing/full_format_recipes.json')
        ingredients = pd.read_csv('../python model/data/ingredient_info.tsv', delimiter='\t')['ingredient name']

        matching_recipes = []

        for recipe in recipes.values: # for each recipe in Epicurios recipes
            matching_ingredients = 0

            if type(recipe[6]) is not list:
                continue

            for id, recipe_ingredient in enumerate(recipe[6]): # for each ingredient in the ingredient list from Epicurios recipes
                for ingredient in ingredients:# for each ingredient in compounds data set
                    if (' ' + ingredient.replace('_', ' ') + ' ') in (recipe_ingredient + ' ').lower() or (' ' + ingredient.replace('_', ' ') + ',') in recipe_ingredient.lower():
                        recipe[6][id] = [ingredient.replace('_', ' '), recipe_ingredient]
                        matching_ingredients += 1
                        break

            if matching_ingredients == len(recipe[6]):
                matching_recipes.append(recipe.tolist())

        # print(str(len(matching_recipes)) + " recipes have matching ingredients")

        return matching_recipes


    def feed_data_to_database(self):

        recipes = self.get_matching_recipes()
        for recipe in recipes:

            recipe_obj = Recipe(title = recipe[10], date_published = recipe[2], rating = recipe[8])
            recipe_obj.save()

            for category_name in recipe[1]:
                category = None
                try:
                    category = Category.objects.get(name = category_name)
                except:
                    category = Category(name = category_name)
                    category.save()
                rc = RecipeCategory(recipe = recipe_obj, category = category)
                rc.save()

            for id, direction_item in enumerate(recipe[4]):
                direction = Direction(content = direction_item, recipe = recipe_obj, order = (id+1))
                direction.save()

            for detailed_ingredient in recipe[6]:
                ingr = Ingredient.objects.get(name = detailed_ingredient[0])
                dg = DetailedIngredient(recipe = recipe_obj, name = detailed_ingredient[1], ingredient = ingr)
                dg.save()
