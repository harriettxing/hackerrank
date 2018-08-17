import math
import os
import random
import re
import sys

centerValue = 5
middleValues = [1, 9, 3, 7]
mv1 = [1, 9]
mv2 = [3, 7]

cv1 = [[1,3,8], [1,7,6], [7,9,2], [3,9,4]]

# computeCost(s1, s)
def computeCost(s1, s):
    cost = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            cost += abs(s1[i][j] - s[i][j])
    return cost

# getLeadingV(i,j)
def getLeadingV(i,j):
    for line in cv1:
        if ((i in line) and (j in line)):
            return line[2]
            
# getMagicSquare(i, j)
#     return a magic square where 3 values are set for square[0][0], square[0][1], square[1][1]
def getMagicSquare(i, j):
    ms = [[0, i, 0], [j, centerValue, 10-j], [0, 10-i, 0]]
    ms[0][0] = getLeadingV(i,j)
    ms[2][0] = 15 - ms[0][0] - ms[1][0]
    ms[2][2] = 15 - ms[2][0] - ms[2][1]
    ms[0][2] = 15 - ms[0][0] - ms[0][1]
    #print(i,j)
    #print(ms)
    return ms

# getMagicSquares(i)
#     returns the two possible magic squares with center value is 5, and square[0,1] is i

def getMagicSquares(i): 
    s = []
    if i in mv1:
        for j in mv2:
            m1 = getMagicSquare(i, j)
            s.append(m1)
    else:
        for j in mv1:
            m2 = getMagicSquare(i, j)
            s.append(m2)
                
    #print(s)
    return s
    
# allMagicSquares(s1)
def allMagicSquares():
    
    s1 = []
    for i in middleValues:
        # print(i)
        s2 = getMagicSquares(i)
        s1 = s1 + s2
        # print(s1)
    return s1

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    min = 0
    # print(s)
    
# create a list of 2D arrays that holds all possible magic squares
    allCombo = allMagicSquares()
    #print(allCombo)

# iterate through allCombo, compute cost for each, tracks the min cost
    min = sys.maxsize
    for i in allCombo:
        c1 = computeCost(i, s)
        #print(i)
        #print(c1)
        if (c1 < min):
            min = c1
    
    print(min)
    return min
    
if __name__ == '__main__':

    s = []

    for _ in range(3):
        c = input().rstrip()
        b = c.split()
        a = map(int, b)
        s.append(list(a))

    result = formingMagicSquare(s)

