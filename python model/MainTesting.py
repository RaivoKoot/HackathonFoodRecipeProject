#from sklearn import datasets
from foodData import FoodData
from dataPreparation import DataPreparation
from compoundEvaluator import CompoundEvaluator
from ingredientMatcher import IngredientMatcher
import numpy as np

############################
# the code is commented out in multiline comments because
# it only needs to be executed once and saves every
# new data in files to be used externally


# load datasets into foodData object
datasetContainer = FoodData()
datasetContainer.importIngredientDataSet('ingredient_info.tsv')
#datasetContainer.importCompoundDataSet('compound_info.tsv')
datasetContainer.importIngredientsCompoundstDataSet('ingredients_compounds.tsv')

'''
# prepare data for algorithm
datasetPreparer = DataPreparation()
datasetPreparer.addMatchUniquenessColumn(datasetContainer)
'''

# label each pair of ingredient and compound with uniqueness value
# using tf-idf algorithm
'''
compoundEvaluator = CompoundEvaluator()
compoundEvaluator.computeIDF(datasetContainer)
compoundEvaluator.assignUniquenesses(datasetContainer)
'''

'''
datasetContainer.exportMatchesToFile()
datasetContainer.importMatches()
'''

#print(datasetContainer.ingredientsCompoundsDataSet)

# fills the ingredient-compound matching matrix with their calculated idfs

ingredientMatcher = IngredientMatcher()
'''
ingredientMatcher.fitIDFMatrix(datasetContainer)
'''


# saves filled matchingMatrix in a csv file
'''
datasetContainer.exportCompoundMatrix()
'''

'''
datasetContainer.importCompoundMatrix()
'''

# get a comparison matrix of all ingredients
'''
ingredientMatcher.computeIngredientMatrix(datasetContainer)
datasetContainer.exportIngredientMatrix()
'''
