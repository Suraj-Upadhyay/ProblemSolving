#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    num = 0
    a.sort()
    j = k = 0
    print(a)
    for i,x in enumerate(a) :
        if abs(x-a[j]) >= 2 :
            j = i
            k = i
        if num < k - j + 1 :
            num = k - j + 1
        k += 1
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
