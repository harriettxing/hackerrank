import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

# loop through arr, find the sum, max, min
    sum = 0
    max = 0
    min = sys.maxsize
    for i in arr:
        sum += i
        if (i > max):
            max = i
        if (i < min):
            min = i
            
    print(str(sum - max) + " " + str(sum - min))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
