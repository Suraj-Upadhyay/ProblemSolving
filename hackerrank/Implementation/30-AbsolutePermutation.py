#!/bin/python3

import math
import os
import random
import re
import sys

def absolutePermutation(n, k):
    if k == 0 :
        return [i for i in range(1,n+1)]
    if n%2 != 0:
        return [-1]
    if k > n//2  or n%k != 0 or (n//k)%2 != 0:
        return [-1]
    isEmpty = [True for i in range(n+1)]
    answer = [i for i in range(n+1)]
    for i in answer[1:n-k+1] :
        if isEmpty[i] :
            answer[i],answer[i+k] = answer[i+k],answer[i]
            isEmpty[i] = False
            isEmpty[i+k] = False
    if answer[n] != n-k :
        return [-1]
    return answer[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
