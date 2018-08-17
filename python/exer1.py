import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    r = [0, 0]    
    for i in range(3):
        if (a[i] > b[i]):
            r[0] = r[0] + 1
        elif (a[i] < b[i]):
            r[1] = r[1] + 1
    return r


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(result)
