#가능한 모든 경우 실행
#n: 선택된 숫자의 개수(길이)
#구해야 할 것: 길이 M짜리 수열

def dfs(n, lst):
    #종료조건
    if n == M:
        ans.append(lst)
        return ans

    for j in range(1, N+1):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, lst+[j])
            visited[j] = 0


N, M = map(int, input().split()) #1~N 자연수 중 중복 없이 M개 고른 수열 (사전 순으로 증가하게 출력)
ans = [] #정답 리스트를 저장할 리스트
visited = [0] * (N+1) #중복을 확인할 리스트
dfs(0, [])
for lst in ans:
    print(*lst)