a, b, c = map(int, input().split())

dice = []
dice.append(a)
dice.append(b)
dice.append(c)

if a == b == c:
    print(10000+a*1000)

elif a == b or b == c or a == c:
    if a == b:
        print(1000+a*100)
    else:
        print(1000+c*100)

elif a != b != c:
    print(max(dice)*100)
