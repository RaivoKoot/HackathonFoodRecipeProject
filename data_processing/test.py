import pandas as pd

recipes = pd.read_json('full_format_recipes.json')
ingredients = pd.read_csv('../python model/data/ingredient_info.tsv', delimiter='\t')['ingredient name']

matches = 0
all = 0
matching_recipes = []
print(recipes.values[22][2])
for recipe in recipes.values: # for each recipe in Epicurios recipes
    matching_ingredients = 0

    if type(recipe[6]) is not list:
        continue

    for recipe_ingredient in recipe[6]: # for each ingredient in the ingredient list from Epicurios recipes
        for ingredient in ingredients :# for each ingredient in compounds data set
            if (' ' + ingredient.replace('_', ' ') + ' ') in (recipe_ingredient + ' ').lower() or (' ' + ingredient.replace('_', ' ') + ',') in recipe_ingredient.lower():
                matching_ingredients += 1
                break

    if matching_ingredients == len(recipe[6]):
        matching_recipes.append(recipe)

recipe_ingredients = dict()

for recipe in matching_recipes:
    for recipe_ingredient in recipe[6]: # for each ingredient in the ingredient list from Epicurios recipes
        recipe_ingredients[recipe_ingredient] = 0
        for ingredient in ingredients :# for each ingredient in compounds data set
            if (' ' + ingredient.replace('_', ' ') + ' ') in (recipe_ingredient + ' ').lower() or (' ' + ingredient.replace('_', ' ') + ',') in recipe_ingredient.lower():
                recipe_ingredients[recipe_ingredient] += 1
                break



with open('ingredient_occurrance.txt', 'w') as f:
    for key in recipe_ingredients:
        if recipe_ingredients[key] == 0:
            f.write("%s - %i\n" % (key, recipe_ingredients[key]))

print(str(len(matching_recipes)) + " recipes have matching ingredients")
