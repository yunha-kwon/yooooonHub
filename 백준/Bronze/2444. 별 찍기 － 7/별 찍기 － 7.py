N = int(input())

for i in range(2*N):
    if i < N:
        print(' ' * (N-i-1) + "*" * (2*i+1))
    elif i > N:
        i = (2 * N - 1) - i
        print(' ' * (N-i-1) + "*" * (2*i+1))