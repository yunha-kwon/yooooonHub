a, b, c = map(int, input().split())
lst = []
lst.append(a)
lst.append(b)
lst.append(c)
lst.sort()

if lst[0] + lst[1] <= lst[2]:
    lst[2] = lst[0] + lst[1] - 1

print(sum(lst))