#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    A = [0 for x in range(26)]
    B = [0 for x in range(26)]
    for x in s1 :
        A[ord(x)-97] += 1
    for x in s2 :
        B[ord(x)-97] += 1
    result = 0
    for i in range(26) :
        result += abs(A[i]-B[i])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
