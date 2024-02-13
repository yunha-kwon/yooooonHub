A, B = map(int, input().split())

def gcd(A, B):
    while B:
        mod = B
        B = A % B
        A = mod
    return A

print(A*B//gcd(A, B))