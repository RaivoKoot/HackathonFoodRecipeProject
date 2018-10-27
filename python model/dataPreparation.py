from matrixoperations import MatrixOperations
import pandas

class DataPreparation:
    matrixOps = MatrixOperations()

    def __init__(self):
        pass

    # adds a default column of zeros to the end of
    # foodData.ingredientsCompoundsDataSet
    # This value will later denote the uniqueness of
    # the compound in the ingredient based off of tf-idf
    def addMatchUniquenessColumn(self, foodData):
        foodData.ingredientsCompoundsDataSet.insert(2,'Uniqueness', 0)

        print(foodData.ingredientsCompoundsDataSet)
