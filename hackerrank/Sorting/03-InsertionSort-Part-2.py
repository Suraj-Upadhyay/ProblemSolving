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

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,n):
        tmp=arr[i]
        j=i-1
        while j>=0:
            if arr[j]<arr[i]:
                break
            j-=1
        j+=1
        for k in range(i,j,-1):
            arr[k]=arr[k-1]
        arr[j]=tmp
        display(arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
