#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    modArray = [x%k for x in s]
    count = [0 for i in range(k)]
    for x in modArray :
        count[x] += 1
    answer = 0
    i = 1
    while i < k/2 :
        answer += max(count[i],count[k-i])
        i += 1
    if count[0] :
        answer += 1
    if k%2==0 :
        if count[k//2] :
            answer += 1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
