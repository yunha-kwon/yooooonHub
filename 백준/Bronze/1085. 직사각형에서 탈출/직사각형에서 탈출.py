x, y, w, h = map(int, input().split())
lst = []
lst.append(w-x)
lst.append(h-y)
lst.append(x)
lst.append(y)

print(min(lst))