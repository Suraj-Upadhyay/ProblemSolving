#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    asqrt = math.floor(math.sqrt(a))
    bsqrt = math.floor(math.sqrt(b))
    if asqrt**2 == a :
        return bsqrt-asqrt+1
    return bsqrt-asqrt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
