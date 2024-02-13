import math

def isPrime(x): #소수판별 함수
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True: #입력받기
    n = int(input())
    if n == 0:
        break
    cnt = 0 #소수의 개수 저장할 변수
    for i in range(n+1, 2*n+1):
        if isPrime(i):
            cnt += 1
    print(cnt)