import sys

N = int(sys.stdin.readline())
num_cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_cards = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in range(len(num_cards)):
    dic[num_cards[i]] = 0

for i in range(M):
    if check_cards[i] not in dic:
        print(0, end=' ')
    else:
        print(1, end=' ')