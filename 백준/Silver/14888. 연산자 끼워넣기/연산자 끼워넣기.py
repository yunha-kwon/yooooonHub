n = int(input())
num_lst = list(map(int, input().split()))
plus, minus, mult, div = map(int, input().split())

mn = 1000000001
mx = -1000000000

def dfs(i, lst):
    global plus, minus, mult, div, mn, mx

    if i == n:
        mx = max(mx, lst)
        mn = min(mn, lst)

    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, lst+num_lst[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, lst-num_lst[i])
            minus += 1
        if mult > 0:
            mult -= 1
            dfs(i+1, lst*num_lst[i])
            mult += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(lst/num_lst[i]))
            div += 1

dfs(1, num_lst[0])
print(mx)
print(mn)