import pandas as pd

def get_matching_recipes():
    recipes = pd.read_json('full_format_recipes.json')
    ingredients = pd.read_csv('../python model/data/ingredient_info.tsv', delimiter='\t')['ingredient name']
    print(list(ingredients.values))

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
        if len(matching_recipes) == 10:
            break

    print(str(len(matching_recipes)) + " recipes have matching ingredients")

    return matching_recipes


def feed_data_to_database():
    recipes = get_matching_recipes()
    print(recipes[5][6])
    print('done')


if __name__ == "__main__":
    feed_data_to_database()
