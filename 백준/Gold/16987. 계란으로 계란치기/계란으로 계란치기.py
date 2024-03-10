#계란으로 계란치기
ans = 0
def break_eggs(eggs, cur_pos): #계란의 내구도-무게 정보가 담긴 리스트 & 현재 계란의 위치
    global ans
    if cur_pos == len(eggs):
        cnt = 0
        for i in range(len(eggs)):
            if eggs[i][0] <= 0:
                cnt += 1
        ans = max(cnt, ans)
        return

    if eggs[cur_pos][0] <= 0:
        break_eggs(eggs, cur_pos+1)

    else:
        broken = False
        for i in range(len(eggs)):
            if i == cur_pos or eggs[i][0] <= 0:
                continue
            eggs[cur_pos][0] -= eggs[i][1]
            eggs[i][0] -= eggs[cur_pos][1]
            broken = True
            break_eggs(eggs, cur_pos+1)
            eggs[cur_pos][0] += eggs[i][1]
            eggs[i][0] += eggs[cur_pos][1]
        if not broken:
            break_eggs(eggs, cur_pos+1)


N = int(input())

eggs = []
for _ in range(N):
    d_and_w = list(map(int, input().split()))
    eggs.append(d_and_w)
break_eggs(eggs, 0)
print(ans)
