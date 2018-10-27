from foodData import FoodData
from matrixoperations import MatrixOperations

# this class uses the concept of the tf-idf algorithm
# to find out how unique each ingredient-substance match is
#
# uniqueness of substances in the ingredients can
# then be used to cluster ingredients that are alike
# based on unique ingredients they have in common
class IngredientMatcher:
    matrixOps = MatrixOperations()

    def __init__(self):
        pass

    def computeUniquenesses(self, foodData):
        ingredients = foodData.ingredientDataSet
        compounds = foodData.compoundDataSet
        matches = foodData.ingredientsCompoundsDataSet

    def computeDocumentFrequency(self, foodData):
        compounds =  foodData.compoundDataSet
        matches = foodData.ingredientsCompoundsDataSet
        frequencies = foodData.documentFrequencyCompounds

        compoundIDs = matrixOps.getColumnOfMatrixAsList(compounds.values, 0)
        matchCompoundIDs = matrixOps.getColumnOfMatrixAsList(matches.values, 1)

# compound[0]
        for compound in compoundIDs:
            pass


    def countCompoundFrequency(self, compoundID, matches):
        frequency = 0

        for match in matches['']:
            if match
