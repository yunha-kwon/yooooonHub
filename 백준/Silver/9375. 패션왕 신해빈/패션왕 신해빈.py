t = int(input())
for _ in range(t):
    n = int(input())
    closet = {}
    for _ in range(n):
        cloth_name, cloth_type = input().split()
        if cloth_type not in closet.keys(): #옷장에 해당 의상 종류가 없다면
            closet[cloth_type] = 1 #새로 추가
        else: #이미 있다면
            closet[cloth_type] += 1 #해당 의상 종류의 카운트 +1

    cnt = 1
    for val in closet.values():
        cnt *= (val+1)

    print(cnt-1) #공집합 제외
