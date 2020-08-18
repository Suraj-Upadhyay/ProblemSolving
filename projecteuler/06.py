sumofsquares = 0
naturalsum = 0
for i in range(1, 101):
    naturalsum += i
    sumofsquares += i * i

print((naturalsum ** 2) - sumofsquares)
