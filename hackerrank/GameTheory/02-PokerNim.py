#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pokerNim function below.
def pokerNim(k, c):
    nimsum = 0
    for x in c:
        nimsum ^= x
    if nimsum:
        return 'First'
    return 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        c = list(map(int, input().rstrip().split()))

        result = pokerNim(k, c)

        fptr.write(result + '\n')

    fptr.close()
