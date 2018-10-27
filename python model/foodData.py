from matrixoperations import MatrixOperations
import pandas

class FoodData:
    matrixOps = MatrixOperations()

    def __init__(self):
        self.ingredientDataSet = None
        self.compoundDataSet = None
        self.ingredientsCompoundsDataSet = None
        self.documentFrequencyCompounds = [0] * 1107

    def importIngredientDataSet(self, fileName):
        self.ingredientDataSet = self.importAndGetDataSet(fileName)

    def importCompoundDataSet(self, fileName):
        self.compoundDataSet = self.importAndGetDataSet(fileName)

    def importIngredientsCompoundstDataSet(self, fileName):
        self.ingredientsCompoundsDataSet = self.importAndGetDataSet(fileName)

    def importAndGetDataSet(self, fileName):
        return self.matrixOps.importDataFromFile('data\\'+fileName)
