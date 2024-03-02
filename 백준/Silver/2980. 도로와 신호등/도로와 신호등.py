n , l = map(int,input().split()) #신호등 개수, 도로의 길이

now = 0
total = 0
for _ in range(n):
    d, r, g = map(int,input().split()) #위치, 빨간불, 초록불
    total += d - now
    now = d
    if total % (r + g) <= r :
        total += r - total % (r + g)

total += l - now
print(total)