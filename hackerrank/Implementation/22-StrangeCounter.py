#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    initial = 3
    a = 0
    while a < t :
        a = a + initial
        initial *= 2
    return a-t+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
