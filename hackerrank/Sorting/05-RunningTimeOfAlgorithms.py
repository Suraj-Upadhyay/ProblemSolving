#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    arrLen = len(arr)
    count=0
    for i in range(1,arrLen):
        item=arr[i]
        j=i-1
        while j>=0 and arr[j] > item:
            arr[j+1]=arr[j]
            count+=1
            j-=1
        j+=1
        arr[j]=item
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
