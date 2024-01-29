n = int(input())

for _ in range(n):
    repeatNum, word = input().split()
    for x in word:
        print(x * int(repeatNum), end='')
    print()