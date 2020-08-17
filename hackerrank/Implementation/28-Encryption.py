#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    words = s.split(' ')
    s = ''.join(words)
    cols = math.ceil(math.sqrt(len(s)))
    matrix = []
    i = 0
    while i < len(s) :
        lim = i + cols
        row = []
        while i < lim :
            if i < len(s) :
                row.append(s[i])
            else :
                row.append(' ')
            i += 1
        matrix.append(row)
    answer = [[] for k in range(cols)]
    for x in matrix :
        x = (''.join(x)).strip()
        for i,y in enumerate(x) :
            answer[i].append(y)
    for i in range(len(answer)) :
        answer[i] = ''.join(answer[i]).strip()
    return ' '.join(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
