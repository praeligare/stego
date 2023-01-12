## Import

import random

## Constant

cst_n = 3 #256
cst_grayLength = 256
cst_alpha = 1 #0.1
cst_h = 4
cst_w = 10

## Function

def createRandomImage():
    randomImage = []
    for i in range(cst_n):
        line = []
        for j in range(cst_n):
            line.append(random.randint(0, cst_grayLength-1))
        randomImage.append(line)
    return randomImage

def transformMatrixToVector(matrix):
    vector = []
    for i in range(cst_n):
        for j in range(cst_n):
            vector.append(matrix[i][j])
    return vector

def transformVectorToMatrix(vector):
    matrix = []
    for i in range(cst_n):
        matrix.append([])
        for j in range(cst_n):
            matrix[i].append(vector[i*cst_n + j])
    return matrix

def leastSignificantBitOfNumber(number):
    return number%2

def leastSignificantBitForVector(vector):
    result = []
    for i in range(len(vector)):
        result.append(leastSignificantBitOfNumber(vector[i]))
    return result

def createX(image):
    return leastSignificantBitForVector(transformMatrixToVector(image))

def createSubH():
    subH = [[1, 0], [1, 1]]
    return subH

def createH(subH):
    return

def createRandomM():
    m = []
    for i in range(cst_n*cst_alpha):
        m.append(random.randint(0,1))
    return m

def codeTrellis(H, x):
    return

def createStegoImage(image, x, y):
    stegoImage = []
    differenceVector = []
    for i in range(len(x)):
        differenceVector.append(y[i] - x[i])
    differenceMatrix = transformVectorToMatrix(differenceVector)
    for i in range(len(image)):
        stegoImage.append([])
        for j in range(len(image[0])):
            stegoImage[i].append(image[i][j] + differenceMatrix[i][j])
    return stegoImage

def showResult(image, stegoImage):
    return

## Initialise Data

v_image = createRandomImage()
v_subH = createSubH()
v_H = createH(v_subH)
v_m = createRandomM()

## Play

v_x = createX(v_image)
v_y = codeTrellis(v_H, v_x)
#v_stegoImage = createStegoImage(v_image, v_x, v_y)
#showResult(v_image, v_stegoImage)