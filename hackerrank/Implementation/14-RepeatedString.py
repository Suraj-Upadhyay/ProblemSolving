#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    slen = len(s)
    totA = 0
    for x in s :
        if x == 'a' :
            totA += 1
    answer = totA*(n//slen)
    n %= slen
    for x in s[:n] :
        if x == 'a' :
            answer += 1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
