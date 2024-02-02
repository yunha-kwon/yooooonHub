# 스택 수열
# 뭔 소리야? ...

stack = []
result = []
cnt = 1
flag = True

N = int(input())

for i in range(N):
    num = int(input())

    #입력받은 숫자까지 스택에 넣기
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    #입력받은 숫자랑 스택의 맨 위 숫자가 같을 때 제거함
    if stack[-1] == num:
        stack.pop()
        result.append('-')

    else: #스택 수열을 만들 수 없는 경우
        flag = False
        break


if flag == True:
    for i in result:
        print(i)

else:
    print('NO')