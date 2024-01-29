num1, num2 = map(str, input().split())

reversed_num1 = num1[::-1]
reversed_num2 = num2[::-1]

if reversed_num1 > reversed_num2:
    print(int(reversed_num1))
else:
    print(int(reversed_num2))