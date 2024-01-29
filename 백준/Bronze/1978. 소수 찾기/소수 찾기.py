N = int(input())
nums = list(map(int,input().split()))
cnt = N

for num in nums:
    if num == 1:
        cnt -= 1
        continue
    elif num == 2:
        continue
    for i in range(2, num):
        if (num % i == 0) and (i != num):
            cnt -= 1
            break
            
print(cnt)
