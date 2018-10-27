#from sklearn import datasets
from matrixoperations import MatrixOperations
from foodData import FoodData
from dataPreparation import DataPreparation
from compoundEvaluator import CompoundEvaluator

matrixOps = MatrixOperations()

#ingredientData = matrixOps.importDataFromJSON('data\\full_format_recipes.json')
#titles = ingredientData['title'].values

datasetContainer = FoodData()
datasetContainer.importIngredientDataSet('ingredient_info.tsv')
datasetContainer.importCompoundDataSet('compound_info.tsv')
datasetContainer.importIngredientsCompoundstDataSet('ingredients_compounds.tsv')

datasetPreparer = DataPreparation()
datasetPreparer.addMatchUniquenessColumn(datasetContainer)

compoundEvaluator = CompoundEvaluator()
compoundEvaluator.computeIDF(datasetContainer)
compoundEvaluator.assignUniquenesses(datasetContainer)

# labelled eaech pair of ingredient and compound with uniqueness value
print(datasetContainer.ingredientsCompoundsDataSet)
