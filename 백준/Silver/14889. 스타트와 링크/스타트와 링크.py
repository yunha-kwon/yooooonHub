#백트랙킹... 여전히 어렵다
import sys
input = sys.stdin.readline

def combi(x, n):
    global result
    if x == N // 2:
        s, l = 0, 0 #스타트, 링크
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    s += S[i][j]
                elif not visited[i] and not visited[j]:
                    l += S[i][j]

        result = min(result, abs(s-l))
        return

    else:
        for i in range(n, N):
            if visited[i] == 0:
                visited[i] += 1
                combi(x+1, i+1)
                visited[i] = 0

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
result = 100000
combi(0, 0)
print(result)