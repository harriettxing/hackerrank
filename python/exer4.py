import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    r1 = 0
    r2 = 0
    r3 = 0
    total = len(arr)
    
    for i in arr:
        if (i > 0):
            r1 = r1 + 1
        elif (i < 0):
            r2 = r2 + 1
        else:
            r3 = r3 + 1
            
    print(r1/total)
    print(r2/total)
    print(r3/total)
    
#if __name__ == '__main__':
n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
