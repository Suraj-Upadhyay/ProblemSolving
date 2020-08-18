import math

def is_prime(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True

i = 3
ssum = 2
while i < 2000000:
    if is_prime(i):
        ssum += i
    i += 2
print(ssum)
