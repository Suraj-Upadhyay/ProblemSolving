#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def divergence(s,t) :
    i = 0
    while i < min(len(s),len(t)) :
        if s[i] != t[i] :
            break
        i += 1
    return i

def appendAndDelete(s,t,k) :
    index = divergence(s,t)
    if s == t :
        return 'Yes'
    if s[:index] == t[:index] :
        req1 = len(s) - index 
        req2 = len(t)  - index
        if req1 == 0 :
            if (k-req2) %2 != 0 :
                return 'No'
            else :
                return 'Yes'
        if req1+req2 > k :
            return 'No'
        else :
            return 'Yes'
    if index == 0 :
        req = len(s) + len(t)
        if req > k :
            return 'No'
    else :
        req = len(s) - index + len(t)  - index
        if req != k :
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
