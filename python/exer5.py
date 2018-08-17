import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):

    for i in range(n):
        spaces = ""
        dots = ""    
        for j in range(n-i-1):
            spaces = spaces + " "
        for k in range(i+1):
            dots = dots + "#"
        print(spaces + dots )
        
if __name__ == '__main__':
    n = int(input())
    staircase(n)