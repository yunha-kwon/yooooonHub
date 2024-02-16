N = int(input())
M = int(input())
S = input()

pointer = cnt = result = 0

while pointer < (M-1):
    if S[pointer:pointer+3] == 'IOI':
        cnt += 1
        pointer += 2
        if cnt == N:
            result += 1
            cnt -= 1
    else:
        pointer += 1
        cnt = 0

print(result)