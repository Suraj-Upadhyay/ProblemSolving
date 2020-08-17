#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    if len(s) == 1:
        return 'YES'
    result = 'YES'
    noOdds = 0
    arr = [0 for x in range(26)]
    for x in s :
        arr[ord(x)-97] += 1
    for x in arr :
        if x%2==1 :
            noOdds += 1
    if (noOdds > 2) :
        result = 'NO'
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
