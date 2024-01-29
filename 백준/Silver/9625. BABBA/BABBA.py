K = int(input())
cnt_A = 0
cnt_B = 1
for i in range(1, K):
    cnt_A, cnt_B = cnt_B, cnt_A + cnt_B

print(cnt_A, cnt_B)