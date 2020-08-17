#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mMax = max(arr)
    mMin = min(arr)
    mSum = sum(arr)
    print(mSum-mMax,mSum-mMin)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
