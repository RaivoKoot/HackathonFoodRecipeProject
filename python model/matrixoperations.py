# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:16:14 2018

@author: Raivo Koot
"""
import numpy as np
import pandas

class MatrixOperations:

    # manually initialize vector
    # np.matrix([[2],[2],[2],[2],[2]]).A
    def __init__(self):
        pass

    def multiplyMatrices(self, matrixA, matrixB):
        result = matrixA @ matrixB
        return result

    def getTranspose(self,matrix):
        return matrix.T

    def scanDataFrameFromFile(self,fileName):
        data = pandas.read_table(fileName)
        return data

    def importDataFromJSON(self, fileName):
        return pandas.read_json(fileName)    

    # removes the labesl and indices from the dataset
    # returns data as numpy matrix
    def getMatrixFromDataFrame(self,dataFrame):
        return dataFrame.values

    def getElementAt(self,dataMatrix, row, column):
        return dataMatrix.item((row,column))

    # returns a new matrix with a new column at the very start with 1's
    def addColumnOfOnes(self,matrix):
        return np.insert(matrix, 0, 1, axis=1)

    def cutOffYColumn(self,matrix):
        return np.delete(matrix,-1,axis=1)

    def getYColumn(self, matrix):
        return self.getColumnOfMatrix(matrix,-1)

    def subtractElements(self,matrixA, matrixB):
        return np.subtract(matrixA,matrixB)

    def squareAllElements(self,matrix):
        return np.square(matrix)

    def getSumOfElements(self,array):
        return np.sum(array)

    def getAmountOfElements(self,array):
        return array.size

    def getThetaVector(self,rows):
        theta = np.full((rows,1), 0)
        return theta

    # index starting at 0
    def getColumnOfMatrix(self,matrix, column):
        columnVector = matrix[:,column]
        columnVector = columnVector.reshape((columnVector.shape[0],1))
        return columnVector

    def listToVector(self, list):
        list = np.asarray(list)
        list = list.reshape((list.shape[0],1))

        return list
