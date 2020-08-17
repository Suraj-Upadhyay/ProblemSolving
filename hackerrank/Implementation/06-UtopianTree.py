#!/bin/python3

import math
import os
import random
import re
import sys

lookup = [-1 for i in range(61)]
lookup[0] = 1
def utopianTree(n):
    if lookup[n] != -1 :
        return lookup[n]
    if n % 2 == 0 :
        lookup[n] = 1 + utopianTree(n-1)
    else :
        lookup[n] = 2*utopianTree(n-1)
    return lookup[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
