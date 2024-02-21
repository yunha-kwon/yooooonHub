N = int(input()) #진짜 약수의 개수
real_factors = list(map(int, input().split()))
real_factors.sort()

if len(real_factors) == 1:
    print((int(*real_factors) ** 2))

elif len(real_factors) >= 2:
    print(real_factors[0] * real_factors[-1])