import math

def is_prime(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True

lcm = 1
for i in range(2, 21):
    if is_prime(i):
        pow = 1
        while (i ** pow) <= 20:
            pow += 1
        lcm *= i ** (pow - 1)
print(lcm)
