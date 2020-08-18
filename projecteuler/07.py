import math

def is_prime(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True

i = 1
count = 0
while count != 10001:
    i += 1
    if is_prime(i):
        count += 1
print(i)
