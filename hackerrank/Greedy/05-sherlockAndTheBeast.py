#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    fives = threes = 0
    if n % 3 == 0:
        fives = n // 3
        threes = 0
    elif n % 3 == 2:
        fives = n // 3 - 1
        threes = 1
    else:
        fives = n // 3 - 3
        threes = 2
    if fives < 0 or threes < 0 or (fives == 0 and threes == 0):
        print(-1)
    else:
        answer = ['5' for i in range(fives * 3)] + ['3' for i in range(threes * 5)]
        for x in answer:
            print(x, end='')
        print()

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
