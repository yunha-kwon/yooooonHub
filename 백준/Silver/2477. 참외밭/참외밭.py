n = int(input())

info_lst = [] #육각형 참외밭 정보를 담는 리스트
for i in range(6):
    d, l = map(int, input().split()) #방향, 길이
    info_lst.append([d, l])

mx_garo = 0
mx_garo_idx = 0
mx_sero = 0
mx_sero_idx = 0
for i in range(len(info_lst)):
    if info_lst[i][0] == 1 or info_lst[i][0] == 2: #동쪽 혹은 서쪽 방향 (가로방향)
        if mx_garo < info_lst[i][1]:
            mx_garo = info_lst[i][1]
            mx_garo_idx = i

    elif info_lst[i][0] == 3 or info_lst[i][0] == 4: #남쪽 혹은 북쪽 방향 (세로방향)
        if mx_sero < info_lst[i][1]:
            mx_sero = info_lst[i][1]
            mx_sero_idx = i

#최장가로길이, 최장세로길이와 인접하지 않는 두 변의 인덱스 구하기
a = (mx_garo_idx + 3) % 6
b = (mx_sero_idx + 3) % 6

big_rect = mx_garo * mx_sero
small_rect = info_lst[a][1] * info_lst[b][1]

print((big_rect-small_rect) * n)