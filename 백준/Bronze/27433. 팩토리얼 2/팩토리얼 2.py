def factorial(n):
    if n <= 1:
        res = 1
    else:
        res = factorial(n-1) * n

    return res

print(factorial(int(input())))