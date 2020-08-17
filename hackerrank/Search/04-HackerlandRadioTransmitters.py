#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(arr, k):
    count = 0
    i = 0
    arr.sort()
    while i < len(arr) :
        mRange = k
        while i < len(arr) - 1 :
            diff = abs(arr[i+1] - arr[i])
            mRange -= diff
            if mRange < 0 :
                break
            i += 1
        mRange = k
        while i < len(arr)- 1 :
            diff = abs(arr[i+1] -arr [i])
            mRange -= diff
            if mRange < 0 :
                break
            i += 1
        count += 1 
        i += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
