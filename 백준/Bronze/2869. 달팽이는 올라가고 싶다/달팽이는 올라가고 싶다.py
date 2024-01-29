A, B, V = map(int, input().split())
#총 높이에서 마지막 날 오른 A만큼 빼고 하루에 오르는 양 (A-B)로 나누면
#마지막 날을 제외한 식 + 1
day = (V - A) / (A - B) + 1

if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)