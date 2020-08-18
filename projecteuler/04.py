def is_palindrome(num):
    num = str(num)
    for i in range(0, len(num) // 2):
        if num[i] != num[len(num) - i - 1]:
            break
    else:
        return True
    return False

palindromes = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if is_palindrome(i * j):
            palindromes.append(i * j)

print(max(palindromes))