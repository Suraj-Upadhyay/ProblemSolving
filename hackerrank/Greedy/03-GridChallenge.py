#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    mGrid = []
    for x in grid :
        p = list(map(str,x))
        p.sort()
        mGrid.append(p)
    n = len(mGrid)
    m = len(mGrid[0])
    i = 0
    while i < m :
        j = 0
        while j < n-1 :
            if mGrid[j][i] > mGrid[j+1][i] :
                return 'NO'
            j += 1
        i += 1
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
