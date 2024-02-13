import sys
from math import gcd #최대공약수

N = int(sys.stdin.readline()) #나무 수 입력

a = int(sys.stdin.readline()) #첫번째 나무 좌표 입력
arr = []

for i in range(N-1): 
    num = int(sys.stdin.readline()) #두번째 나무부터 마지막 나무까지 입력
    arr.append(num - a) #본인 앞 나무와의 거리 차이를 arr 배열에 추가
    a = num 

g = arr[0] #첫번째 나무 좌표
for i in range(1, len(arr)): #두번째 나무부터 마지막 나무까지 순회
    g = gcd(g, arr[i]) #최대공약수 구하기

result = 0
for i in arr: #배열 순회
    result += i // g - 1 #거리 차 // 최대공약수 -1 한 것을 모두 더한 것이 결과

print(result) #결과 출력
