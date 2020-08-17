#!/bin/python3

import os
import sys

#
# Complete the aOrB function below.
#
def hexChange(a,b,c) :
    a = bin(int(a,16))[2:]
    b = bin(int(b,16))[2:]
    c = bin(int(c,16))[2:]
    d = ['0' for i in range(4-len(a))]
    e = ['0' for i in range(4-len(b))]
    f = ['0' for i in range(4-len(c))]
    d.extend(a)
    e.extend(b)
    f.extend(c)
    a,b,c = d,e,f
    changeOfBits = 0
    for i in range(4) :
        if int(a[i]) | int(b[i]) != int(c[i]) :
            if int(c[i]) == 1 :
                b[i] = '1'
                changeOfBits += 1
            elif int(c[i]) == 0 :
                if a[i] == '1' :
                    a[i] = '0'
                    changeOfBits += 1
                if b[i] == '1' :
                    b[i] = '0'
                    changeOfBits += 1
    a = ''.join(a)
    b = ''.join(b)
    return [hex(int(a,2))[2:],hex(int(b,2))[2:],changeOfBits]

def maximizeA(a,b,c,k) :
    a = bin(int(a,16))[2:]
    b = bin(int(b,16))[2:]
    c = bin(int(c,16))[2:]
    d = ['0' for i in range(4-len(a))]
    e = ['0' for i in range(4-len(b))]
    f = ['0' for i in range(4-len(c))]
    d.extend(a)
    e.extend(b)
    f.extend(c)
    a,b,c = d,e,f
    for i in range(4) :
        if k == 0 :
            break
        if k >= 1 and c[i] == '1' and a[i] == '1' and b[i] == '1':
            a[i] = '0'
            k -= 1
        elif k >=2 and c[i] == '1' and a[i] == '1' and b[i] == '0' :
            a[i] = '0'
            b[i] = '1'
            k -= 2
    a = ''.join(a)
    b = ''.join(b)
    return [hex(int(a,2))[2:],hex(int(b,2))[2:],k]

def AorB(k,a,b,c) :
    if max(len(a),len(b)) < len(c) :
        print(-1)
        return
    maxL = max(len(a),len(b),len(c))
    A = ['0' for i in range(maxL-len(a))]
    B = ['0' for i in range(maxL-len(b))]
    C = ['0' for i in range(maxL-len(c))]
    A.extend(a)
    B.extend(b)
    C.extend(c)
    i = 0
    while i < maxL:
        A[i],B[i],changeofBits = hexChange(A[i],B[i],C[i])
        k -= changeofBits
        i += 1
    if k < 0 :
        print(-1)
        return
    if k :
        i = 0
        while i < maxL and k:
            A[i],B[i],k = maximizeA(A[i],B[i],C[i],k)
            i += 1
        pass
    A = ''.join(A)
    B = ''.join(B)
    A = hex(int(A,16))[2:].upper()
    B = hex(int(B,16))[2:].upper()
    print(A)
    print(B)


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        k = int(input())

        a = input()

        b = input()

        c = input()

        AorB(k, a, b, c)
