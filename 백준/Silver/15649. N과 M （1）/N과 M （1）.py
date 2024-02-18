def NandM(i, n, m): # i: answer 배열에 들어온 숫자의 개수
    if i == m:
        print(*answer)
    for j in range(1, n+1):
        if not visited[j]:
            visited[j] = 1
            answer.append(j)
            NandM(i+1, n, m)
            visited[j] = 0
            answer.pop()

n, m = map(int, input().split())
visited = [0] * (n+1)
answer = []

NandM(0, n, m)

