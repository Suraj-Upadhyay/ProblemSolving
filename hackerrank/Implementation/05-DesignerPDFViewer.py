#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxHeight = -1
    letterCount = len(word)
    mMax = max(h)
    for x in word :
        if maxHeight < h[ord(x)-97] :
            maxHeight = h[ord(x)-97]
            if maxHeight == mMax :
                break
    return maxHeight*letterCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
