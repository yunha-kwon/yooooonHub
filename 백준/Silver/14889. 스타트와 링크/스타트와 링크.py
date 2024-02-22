# 백트래킹: 가능한 모든 경우
# 스타트와 링크
# n: 사람 번호(0번 ~ N-1번)
def calc(a_lst, b_lst):
    a_sum = b_sum = 0
    for i in range(M):
        for j in range(M):
            a_sum += team[a_lst[i]][a_lst[j]]
            b_sum += team[b_lst[i]][b_lst[j]]
    return abs(a_sum - b_sum)

def dfs(n, a_lst, b_lst):
    global ans
    # 종료조건
    if n == N:
        if len(a_lst) == len(b_lst): # 같은 인원 수로 팀을 구성
            ans = min(ans, calc(a_lst, b_lst))
        return

    dfs(n+1, a_lst+[n], b_lst) # A팀 선택한 경우
    dfs(n+1, a_lst, b_lst+[n]) # B팀 선택한 경우


N = int(input())
team = [list(map(int, input().split())) for _ in range(N)]

M = N // 2
ans = 100*M*M
dfs(0, [], [])
print(ans)