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

        # matrix comparing ingredients with compounds
        self.compoundMatrix = np.zeros((1533,1107))

        # matrix comparing all ingredients
        self.ingredientMatrix = None

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

    def exportCompoundMatrix(self):
        self.compoundMatrix = pandas.DataFrame(data=self.compoundMatrix)

        self.compoundMatrix.to_csv(path_or_buf='data\\compound_matrix.csv')

    def importCompoundMatrix(self):
        self.compoundMatrix = self.matrixOps.importCSVFromFile('data\\compound_matrix.csv')

    def exportIngredientMatrix(self):
        dataFrame = pandas.DataFrame.from_records(self.ingredientMatrix)
        dataFrame.to_csv(path_or_buf='data\\ingredient_matrix.csv')

    def importIngredientsMatrix(self):
        self.ingredientMatrix = self.matrixOps.importCSVFromFile('data\\ingredient_matrix.csv')
