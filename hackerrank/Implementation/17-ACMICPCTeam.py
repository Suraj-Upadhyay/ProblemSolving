#!/bin/python3

import math
import os
import random
import re
import sys

def knowledgeBin(s:str) -> int:
    count = 0
    for x in s[2:] :
        if x == '1' :
            count += 1
    return count

# Complete the acmTeam function below.
def acmTeam(topic):
    maxKnowledge = 0
    maxTeams = []
    i = 0
    while i < len(topic) :
        j = i+1
        while j < len(topic) :
            knowledge = knowledgeBin(bin(int(topic[i],2)|int(topic[j],2)))
            if maxKnowledge < knowledge:
                maxKnowledge = knowledge
                maxTeams.clear()
                maxTeams.append([i,j])
            elif maxKnowledge == knowledge :
                maxTeams.append([i,j])
            j+=1
        i+=1
    return [maxKnowledge,len(maxTeams)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
