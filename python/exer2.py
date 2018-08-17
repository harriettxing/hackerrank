import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    r = 0
    for a in ar:
        r = r + a;
    return r
    
ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = aVeryBigSum(ar)
print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
