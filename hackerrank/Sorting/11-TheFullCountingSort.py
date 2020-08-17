#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    resultArray = [[] for x in range(100)]
    size = len(arr)
    for i in range(size):
        if i < size//2 :
            arr[i][1] = '-'
        x = int(arr[i][0])
        resultArray[x].append(arr[i][1])
    for x in resultArray:
        for s in x:
            print(s,end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
