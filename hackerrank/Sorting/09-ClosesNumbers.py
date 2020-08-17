#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    resultArray = []
    mMin = arr[len(arr)-1]-arr[0]
    i = 1
    while i < len(arr):
        if arr[i]-arr[i-1] < mMin :
            mMin = arr[i]-arr[i-1]
            resultArray.clear()
        if arr[i]-arr[i-1] == mMin :
            resultArray.append(arr[i-1])
            resultArray.append(arr[i])
        i+=1
    return resultArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
