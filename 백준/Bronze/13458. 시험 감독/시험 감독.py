n = int(input()) #시험장 개수
p = list(map(int, input().split())) #각 시험장에 있는 응시자 수
b, c = map(int, input().split()) #총감독관 / 부감독관

result = 0

for i in range(n):
    p[i] -= b
    result += 1

    if p[i] > 0:
        if p[i] % c == 0:
            result += (p[i] // c)

        else:
            result += (p[i] // c + 1)

print(result)