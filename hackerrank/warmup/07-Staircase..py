#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    space = n-1
    for i in range(1,n+1) :
        for p in range(space) :
            print(end=' ')
        space -= 1
        for x in range(i) :
            print(end = '#')
        print()


if __name__ == '__main__':
    n = int(input())

    staircase(n)
