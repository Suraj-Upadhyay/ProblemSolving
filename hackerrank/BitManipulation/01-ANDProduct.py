#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the andProduct function below.
def andProduct(a, b):
    binary = bin(a)[2:]
    answer = []
    cummulative = 0
    for i,x in enumerate(reversed(binary)) :
        if x == '1' :
            if b >= a+2**i-cummulative :
                answer.append('0')
            else :
                answer.append('1')
        else :
            answer.append('0')
        cummulative += int(x)*2**i
    answer.reverse()
    return int(''.join(answer),2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
