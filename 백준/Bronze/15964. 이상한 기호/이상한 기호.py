def calculate(a, b):
    result = (a+b)*(a-b)
    return result

a, b = map(int, input().split())
print(calculate(a, b))