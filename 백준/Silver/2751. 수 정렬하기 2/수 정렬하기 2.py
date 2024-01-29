N = int(input())
num_lst = []
for i in range(N):
    num_lst.append(int(input()))

num_lst.sort()

for i in num_lst:
    print(i)
