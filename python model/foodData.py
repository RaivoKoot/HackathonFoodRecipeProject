from matrixoperations import MatrixOperations
import pandas
import numpy as np

class FoodData:
    matrixOps = MatrixOperations()

    def __init__(self):
        self.ingredientDataSet = None
        self.compoundDataSet = None
        self.ingredientsCompoundsDataSet = None
        self.documentFrequencyCompounds = [0] * 1107

        # matrix that adds every single compound as attribute to ingredient
        self.fullIngredientMatrix = np.zeros((1533,1107))

    def importIngredientDataSet(self, fileName):
        self.ingredientDataSet = self.importAndGetDataSet(fileName)

    def importCompoundDataSet(self, fileName):
        self.compoundDataSet = self.importAndGetDataSet(fileName)

    def importIngredientsCompoundstDataSet(self, fileName):
        self.ingredientsCompoundsDataSet = self.importAndGetDataSet(fileName)

    def importAndGetDataSet(self, fileName):
        return self.matrixOps.importDataFromFile('data\\'+fileName)

    def exportMatchesToFile(self):
        self.ingredientsCompoundsDataSet.to_csv(path_or_buf='data\\matches_unique.csv', index = False)

    def importMatches(self):
        self.ingredientsCompoundsDataSet = self.matrixOps.importCSVFromFile('data\\matches_unique.csv')

    def exportMatchingMatrix(self):
        self.fullIngredientMatrix = pandas.DataFrame(data=self.fullIngredientMatrix)

        self.fullIngredientMatrix.to_csv(path_or_buf='data\\matching_matrix.csv')

    def importMatchingMatrix(self):
        self.fullIngredientMatrix = self.matrixOps.importCSVFromFile('data\\matching_matrix.csv')
