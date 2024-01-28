N = int(input())

if N % 5 == 0: # N이 5의 배수인 경우
    print(N // 5)

else:
    cnt = 0
    while N > 0:
        N -= 3
        cnt += 1

        if N % 5 == 0: # 5kg, 3kg 조합해서 담을 수 있는 경우
            cnt += N // 5
            print(cnt)
            break

        elif N == 1 or N == 2: # 5kg, 3kg로 나눌 수 없는 경우
            print(-1)
            break

        elif N == 0: # N이 3의 배수인 경우
            print(cnt)
            break