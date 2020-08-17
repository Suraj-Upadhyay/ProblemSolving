#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    mMin = min(brr)
    missing = []
    mBrr = [x-mMin for x in brr]
    mArr = [x-mMin for x in arr]
    compB = [0 for x in range(101)]
    compA = [0 for x in range(101)]
    for x in mBrr : 
        compB[x]+=1
    for x in mArr :
        compA[x]+=1
    for i in range(101) :
        if compB[i] != compA[i] :
            missing.append(i)
    return [x + mMin for x in missing]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
