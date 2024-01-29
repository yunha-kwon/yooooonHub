N = int(input())
lst = []
i = 2

while i <= N:
    if N % i == 0:
        lst.append(i)
        N = N / i
    else:
        i += 1

for i in lst:
    print(i)