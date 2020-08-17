#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    result = []
    n -= 1
    for i in range(n+1) :
        result.append(a*i + b*(n-i))
    return sorted(list(set(result)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
