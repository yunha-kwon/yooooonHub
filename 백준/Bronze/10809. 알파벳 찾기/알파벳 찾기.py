s = str(input())
alpha = list(range(97, 123))

for i in alpha:
    print(s.find(chr(i)), end=' ')