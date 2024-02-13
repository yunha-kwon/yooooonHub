#최소공배수 구하는 함수
def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

A, B = map(int, input().split())
C, D = map(int, input().split())
N = gcd(A*D + C*B, B*D) #최소공배수
print((A*D + C*B)//N, B*D//N) #최소공배수로 약분