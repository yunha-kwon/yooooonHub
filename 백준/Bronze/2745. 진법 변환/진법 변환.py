N, B = input().split()
B = int(B)

order = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N_index = []

for i in N:
    N_index.append(order.index(i))

sum = 0
for i in range(len(N)):
    sum += (B ** (len(N_index)-i-1) * N_index[i])

print(sum)