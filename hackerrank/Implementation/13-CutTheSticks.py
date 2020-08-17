#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    answer = []
    sticks = [0 for i in range(1001)]
    for x in arr :
        sticks[x] += 1
    left = len(arr)
    for x in sticks :
        if x :
            answer.append(left)
            left -= x
        if left == 0 :
            break
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
