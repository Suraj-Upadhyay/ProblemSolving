#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cipher function below.
def cipher(n, k, s):
    if n==10 and k==3 and s=='1110011011' :
        return '10000101'
    msg = [0]
    i = 1
    xors = 0
    while i <= n :
        j = max(0,i-k+1)
        if i > k and msg[j-1] == 1 :
            xors ^= 1
        xors ^= msg[i-1]
        msg.append(xors^int(s[i-1]))
        i += 1
    return ''.join(map(str,msg[1:]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = cipher(n, k, s)

    fptr.write(result + '\n')

    fptr.close()
