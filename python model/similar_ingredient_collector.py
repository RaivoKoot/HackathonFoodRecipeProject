import numpy as np
import pandas
from foodData import FoodData

from sklearn.metrics.pairwise import cosine_similarity


class IngredientMatcher:

    def __init__(self):
        pass

    def fitIDFMatrix(self, foodData):
        matches = foodData.ingredientsCompoundsDataSet.values
        compoundMatrix = foodData.compoundMatrix

        for match in matches:
            ingredient_ID = int(match[0])
            compound_ID = int(match[1])
            idf = match[2]

            compoundMatrix[ingredient_ID,compound_ID] = idf

        foodData.compoundMatrix = compoundMatrix

    # uses cosine similarity between two rows to define similarity between
    # two ingredients and returns results as matrix(n_samples,n_samples)
    def computeIngredientMatrix(self, foodData):
        compoundMatrix = foodData.compoundMatrix

        foodData.ingredientMatrix = cosine_similarity(compoundMatrix)
