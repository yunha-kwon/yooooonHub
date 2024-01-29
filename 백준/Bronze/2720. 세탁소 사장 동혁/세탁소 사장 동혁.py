T = int(input())

q = 25
d = 10
n = 5
p = 1
lst = []

for i in range(T):
    C = int(input())
    Q = C // q
    D = C % q // d
    N = C % q % d // n
    P = C % q % d % n // p
    print(Q, D, N, P)