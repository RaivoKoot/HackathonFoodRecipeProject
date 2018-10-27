#from sklearn import datasets
from matrixoperations import MatrixOperations

matrixOps = MatrixOperations()

#ingredientData = matrixOps.scanDataFrameFromFile('data\\full_format_recipes.json')
print("hello")
ingredientData = matrixOps.importDataFromJSON('data\\full_format_recipes.json')

titles = ingredientData['title'].values

for title in titles:
    print(title)
print("hello")
