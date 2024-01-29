M = int(input())
N = int(input())

prime_lst = []

for num in range(M, N+1):
    not_prime = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                not_prime += 1
                break

        if not_prime == 0:
            prime_lst.append(num)

if len(prime_lst) == 0:
    print(-1)
else:
    print(sum(prime_lst))
    print(min(prime_lst))