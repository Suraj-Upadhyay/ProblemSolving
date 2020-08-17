#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh , mm , ss = map(int,s[0:8].split(':'))
    meridian = s[8:10]
    if meridian == 'PM' and not hh == 12:
        hh += 12
    if meridian == 'AM' and hh == 12 :
        hh = 0
    return '{0:02d}:{1:02d}:{2:02d}'.format(hh,mm,ss)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result)

    f.close()
