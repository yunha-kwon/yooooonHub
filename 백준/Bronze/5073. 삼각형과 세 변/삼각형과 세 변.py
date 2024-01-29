while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    lst = []
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()

    if lst[0] + lst[1] <= lst[2]:
        print('Invalid')

    else:
        if a == b == c:
            print('Equilateral')
        elif a == b or a == c or b == c:
            print('Isosceles')
        else:
            print('Scalene')