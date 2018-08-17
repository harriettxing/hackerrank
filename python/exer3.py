import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    
    r1 = 0
    r2 = 0
    for i in range(len(arr)):
        #print(arr[i][i])
        r1 = r1 + arr[i][i]
        j = (i+1)*(-1)
        #print(arr[i][j])
        r2 = r2 + arr[i][j]
    
    r = abs(r1 - r2)
    return r
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()