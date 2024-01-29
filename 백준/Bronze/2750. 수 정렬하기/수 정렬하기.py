N = int(input())
num_lst = []

for i in range(N):
    num = int(input())
    num_lst.append(num)

num_lst.sort()

for i in num_lst:
    print(i)