#from sklearn import datasets
from matrixoperations import MatrixOperations
from foodData import FoodData
from dataPreparation import DataPreparation

matrixOps = MatrixOperations()

#ingredientData = matrixOps.importDataFromJSON('data\\full_format_recipes.json')
#titles = ingredientData['title'].values

datasetContainer = FoodData()

datasetContainer.importIngredientsCompoundstDataSet('ingredients_compounds.tsv')


datasetPreparer = DataPreparation()

datasetPreparer.addMatchUniquenessColumn(datasetContainer)
