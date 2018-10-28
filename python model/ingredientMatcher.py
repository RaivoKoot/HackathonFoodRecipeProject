import numpy as np
import pandas
from foodData import FoodData


class IngredientMatcher:

    def __init__(self):
        pass

    def fitIDFMatrix(self, foodData):
        matches = foodData.ingredientsCompoundsDataSet.values
        matchingMatrix = foodData.fullIngredientMatrix

        for match in matches:
            ingredient_ID = int(match[0])
            compound_ID = int(match[1])
            idf = match[2]

            matchingMatrix[ingredient_ID,compound_ID] = idf

        foodData.fullIngredientMatrix = matchingMatrix
