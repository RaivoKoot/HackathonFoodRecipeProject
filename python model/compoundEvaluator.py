from foodData import FoodData
from matrixoperations import MatrixOperations
import pandas
import math

# this class uses the concept of the tf-idf algorithm
# to find out how unique each ingredient-substance match is
#
# uniqueness of substances in the ingredients can
# then be used to cluster ingredients that are alike
# based on unique ingredients they have in common
class CompoundEvaluator:
    matrixOps = MatrixOperations()

    def __init__(self):
        pass


    def computeUniquenesses(self, foodData):
        ingredients = foodData.ingredientDataSet
        compounds = foodData.compoundDataSet
        matches = foodData.ingredientsCompoundsDataSet

    # FINISHED
    # compute the inverse document frequency for every compound and
    # save it in foodData.documentFrequencyCompounds
    def computeIDF(self, foodData):
        compounds =  foodData.compoundDataSet
        matches = foodData.ingredientsCompoundsDataSet
        frequencies = foodData.documentFrequencyCompounds

        # only get the id colums from each dataset
        compoundIDs = self.matrixOps.getColumnOfMatrixAsList(compounds.values, 0)
        matchCompoundIDs = self.matrixOps.getColumnOfMatrixAsList(matches.values, 1)

        index = 0
        for compoundID in compoundIDs:
            count = self.countCompound(compoundID, matchCompoundIDs)
            count = self.transformDocumentFrequency(count) # idf function

            frequencies[index] = count
            index += 1

        foodData.documentFrequencyCompounds = frequencies
        foodData.ingredientsCompoundsDataSet = matches


    # FINISHED
    # counts how often the id of a compound is found in the
    # compound-ingredient matches. This is the document frequency
    def countCompound(self, compoundID, matchCompoundIDs):
        count = 0

        for compound in matchCompoundIDs:
            if compoundID == compound:
                count += 1

        return count

    # FINISHED
    # idf function
    # returns the log of the inverse of a number, documentFrequency
    def transformDocumentFrequency(self, documentFrequency):
        numberOfIngredients = 1530

        inverse = numberOfIngredients / documentFrequency
        log = math.log(inverse)
        return log

    # assigns the idfs to the last column of
    # ingredientsCompounds labeled uniqueness
    def assignUniquenesses(self, foodData):
        matches = foodData.ingredientsCompoundsDataSet
        frequencies = foodData.documentFrequencyCompounds
        compounds = foodData.compoundDataSet


        # only get the id colums from each dataset
        compoundIDs = self.matrixOps.getColumnOfMatrixAsList(compounds.values, 0)
        matchCompoundIDs = self.matrixOps.getColumnOfMatrixAsList(matches.values, 1)

        #matches.at[index, 'Uniqueness'] =  count
        frequencyIndex = 0
        for compoundID in compoundIDs:
            frequency = frequencies[frequencyIndex]
            frequencyIndex += 1

            matchesIndex = 0
            for matchCompoundID in matchCompoundIDs:
                if(matchCompoundID == compoundID):
                    matches.at[matchesIndex, 'Uniqueness'] =  frequency
                matchesIndex += 1

        print(matches)
