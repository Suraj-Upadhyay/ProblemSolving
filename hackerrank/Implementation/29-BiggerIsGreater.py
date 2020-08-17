#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    i = len(w) - 1
    mMax = i
    while i >= 0 :
        if ord(w[mMax]) > ord(w[i]) :
            break
        elif ord(w[mMax]) < ord(w[i]) :
            mMax = i
        i -= 1
    else :
        return 'no answer'
    answer = [x for x in w]
    j = mMax 
    while j < len(answer) :
        if ord(answer[j]) < ord(answer[mMax]) and ord(answer[j]) > ord(answer[i]) :
            mMax = j
        j += 1
    t = answer[mMax] 
    answer[mMax] = answer[i]
    answer[i] = t
    aux = answer[i+1:]
    aux.sort()
    answer = answer[:i+1] + aux
    return ''.join(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
