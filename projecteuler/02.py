ssum = 0
a, b = 1, 2
while b <= 4000000:
    if b % 2 == 0:
        ssum += b
    b = b + a
    a = b - a
print(ssum)
