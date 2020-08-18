import math
for a in range(1, 1001):
    for b in range(1, 1001):
        c = math.sqrt(a * a + b * b)
        if c + a + b == 1000:
            print(a * b * c)
            exit()
