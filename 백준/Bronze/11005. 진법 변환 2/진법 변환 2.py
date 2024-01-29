N, B = input().split()
N = int(N)
B = int(B)

lst = []

while N:
    lst.append(N % B)
    N = N // B

idx = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans_lst = []
for i in lst[::-1]:
    i = idx[i]
    ans_lst.append(i)

print(*ans_lst, sep='')