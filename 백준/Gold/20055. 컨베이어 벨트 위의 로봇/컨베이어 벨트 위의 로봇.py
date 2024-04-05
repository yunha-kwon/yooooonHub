import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
step = 1

while True:
    # 1
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 #로봇 내리는 위치이므로 0으로 바꿔줌

    # 2
    if robot: #로봇이 존재한다면,
        # i-1이 로봇 내리는 위치 인덱스이므로 그 전 위치인 i-2부터 0까지
        for i in range(n-2, -1, -1):
            # 현 위치에 로봇이 있고, 다음 위치에 로봇이 없고, 다음 위치의 내구도가 1 이상 남아있다면,
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = 1 # 로봇을 다음 칸으로 이동
                robot[i] = 0 # 현 위치에 있던 로봇은 없앰 처리
                belt[i+1] -= 1 # 다음 위치의 내구도 -1
        robot[-1] = 0 # for문 끝났을 때 내리는 위치에 위치한 로봇 out

    # 3
    # 올리는 위치에 로봇이 없고, 칸의 내구도가 0이 아니면,
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1 # 올리는 위치에 로봇을 올림
        belt[0] -= 1 # 올리는 위치의 내구도 -1

    # 4
    # 내구도 0인 위치가 k개 이상이 되면 break
    if belt.count(0) >= k:
        break

    step += 1 # 단계 수 + 1

print(step)
