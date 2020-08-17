#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    plus = minus = zero = 0
    for x in arr :
        if x > 0 :
            plus += 1/n
        elif x < 0 :
            minus += 1/n
        else :
            zero += 1/n
    for x in [plus,minus,zero]:
        print('{0:.6f}'.format(x))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split(' ')))

    plusMinus(arr)
