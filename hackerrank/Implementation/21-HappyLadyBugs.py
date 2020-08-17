#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    i = 1
    if len(b) == 1:
        if b[0] == '_' :
            return 'YES'
        else :
            return 'NO'
    while i <= len(b)-2 :
        if b[i-1] != b[i] and b[i+1] != b[i] :
            break
        i += 1
    else :
        if b[0] == b[1] and b[len(b)-1] == b[len(b)-2] :
            return 'YES'
    blanks = 0
    arr = [0 for x in range(26)]
    for x in b :
        if x == '_' :
            blanks += 1
        else :
            arr[ord(x)-65] += 1
    if blanks == 0 :
        return 'NO'
    for x in arr : 
        if x == 1 :
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
