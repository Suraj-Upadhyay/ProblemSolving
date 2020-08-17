#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luckBal = 0
    impo = [x[0] for x in contests if x[1]==1]
    unimpo = [x[0] for x in contests if x[1]==0]
    luckBal += sum(unimpo)
    impo.sort(reverse=True)
    luckBal += sum(impo[:k])
    luckBal -= sum(impo[k:])
    return luckBal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
