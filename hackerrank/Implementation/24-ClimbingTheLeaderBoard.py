#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rankList = []
    scores = list(set(scores))
    scores.sort(reverse=True)
    for x in alice :
        start = 0
        end = len(scores) - 1
        if x > scores[start] :
            rankList.append(1)
        elif x < scores[end] :
            rankList.append(len(scores) + 1)
        else :
            while start <= end :
                mid = (start+end)//2
                if x == scores[mid] :
                    rankList.append(mid+1)
                    break
                elif x < scores[mid] :
                    if x > scores[mid+1] or mid == len(scores) - 1:
                        rankList.append(mid+2)
                        break
                    start = mid + 1
                else :
                    if x < scores[mid-1] :
                        rankList.append(mid+1)
                        break
                    end = mid - 1
    return rankList

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
