numbers = []
dp = []
for line in open("p067_triangle.txt"):
    n = line.split()
    numbers.append(n)
    dp.append([None for i in range(len(n))])

def bestpath(num: list, i, j):
    if i == len(num) - 1:
        return int(num[i][j])
    if dp[i][j]:
        return dp[i][j]
    a = int(num[i][j]) + bestpath(num, i + 1, j)
    b = int(num[i][j]) + bestpath(num, i + 1, j + 1)
    dp[i][j] = a if a > b else b
    return dp[i][j]

print(bestpath(numbers, 0, 0))
