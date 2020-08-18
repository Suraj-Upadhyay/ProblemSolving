import math

def is_prime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

num = 600851475143
divisors = []
i = 1
while i <= math.sqrt(num):
    if num % i == 0:
        divisors.append(i)
        if is_prime(num // i):
            break
    i += 1
else:
    for x in reversed(divisors):
        if is_prime(x):
            i = x
            break
print(i)
