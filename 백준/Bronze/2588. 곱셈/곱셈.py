num1 = int(input())
num2 = int(input())

num3 = num1 * (num2 % 10)
num4 = int(num1 * (num2 % 100 - num2 % 10) / 10)
num5 = num1 * (num2 // 100)
print(num3)
print(num4)
print(num5)

print(num3 + num4 * 10 + num5 * 100)