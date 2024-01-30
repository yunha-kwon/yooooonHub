import sys

N = int(sys.stdin.readline())
word_lst = []
for i in range(N):
    word_lst.append(sys.stdin.readline().strip())

new_lst = list(set(word_lst))

new_lst.sort() #사전 순
new_lst.sort(key = len) #길이 순

for i in new_lst:
    print(i)