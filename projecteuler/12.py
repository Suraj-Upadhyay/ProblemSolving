def get_divisors(num):
    answer = 0
    i = 1
    while i <= num:
        if num % i == 0:
            answer += 1
        i += 1
    return answer

i = 1
solution = None
while True:
    num1, num2 = i * (2 * i - 1), i * (2 * i + 1)
    if get_divisors(num1) >= 500:
        solution = num1
        break
    elif get_divisors(num2) >= 500:
        solution = num2
        break
    i += 1
print(solution)
