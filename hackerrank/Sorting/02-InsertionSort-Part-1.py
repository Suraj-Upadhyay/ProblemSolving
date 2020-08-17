#!/bin/python3

import math
import os
import random
import re
import sys

def display(arr):
    for x in arr:
        print(x,end=' ')
    print()

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    tmp = arr[n-1];
    pos = n-1
    for x in range(n):
        if arr[x] > tmp:
            pos = x
            break
    i = n-2
    while i>=pos:
        arr[i+1]=arr[i]
        display(arr)
        i-=1
    arr[pos] = tmp
    display(arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
