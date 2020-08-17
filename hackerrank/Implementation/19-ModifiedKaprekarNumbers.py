def kaprekarNumbers(p, q):
    answer = []
    i = p
    while i <= q :
        d = len(str(i))
        string = str(i*i)
        n1 = string[-d:] 
        n2 = string[:-d]
        if len(n1) :
            n1 = int(n1)
        else :
            n1 = 0
        if len(n2) :
            n2 = int(n2)
        else :
            n2 = 0
        if n1 + n2 == i : 
            answer.append(i)
        i += 1
    if len(answer) :
        print(' '.join(map(str,answer)))
    else :
        print('INVALID RANGE')

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)
