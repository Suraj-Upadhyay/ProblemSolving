#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, rq, cq, obstacles):
    horpos = n-cq
    horneg = cq-1
    verpos = n-rq
    verneg = rq-1
    rdpos = min(horpos,verpos)
    rdneg = min(horneg,verneg)
    ldpos = min(horpos,verneg)
    ldneg = min(horneg,verpos)
    answer = [horpos,horneg,verpos,verneg,rdpos,rdneg,ldpos,ldneg]
    for x in obstacles :
        if x[1] == cq :
            if rq-x[0] > 0:
                answer[3] = min(answer[3],rq-x[0]-1)
            elif rq-x[0] < 0 :
                answer[2] = min(answer[2],x[0]-rq-1)
            continue
        elif x[0] == rq :
            if cq-x[1] > 0 :
                answer[1] = min(answer[1],cq-x[1]-1)
            elif cq-x[1] < 0 :
                answer[0] = min(answer[0],x[1]-cq-1)
            continue
        m = (x[1]-cq)/(x[0]-rq)
        if m == 1 :
            if x[0] > rq :
                answer[4] = min(answer[4],x[0]-rq-1)
            elif x[0] < rq :
                answer[5] = min(answer[5],rq-x[0]-1)
        elif m == -1 :
            if x[0] > rq :
                answer[7] = min(answer[7],x[0]-rq-1)
            elif x[0] < rq :
                answer[6] = min(answer[6],rq-x[0]-1)
    return sum(answer)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
