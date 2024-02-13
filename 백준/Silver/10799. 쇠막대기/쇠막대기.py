lst = input() # 쇠 막대기 & 레이저 정보 입력
result = 0 # 잘린 막대기 개수
cnt = 0 # 쌓여있는 막대기 개수

for i in range(len(lst)):
    if lst[i] == '(':  #막대기 추가
        cnt += 1
    else:  # ')'
        cnt -= 1
        if lst[i-1] == '(':  # 레이저
            result += cnt
        else:  # 막대기 끝
            result += 1

print(f'{result}')