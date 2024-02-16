T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    docu = list(map(int, input().split()))
    ord = [i for i in range(N)]

    cnt = 0

    while True:
        if docu[0] == max(docu):
            cnt += 1
            if ord[0] == M:
                print(cnt)
                break
            else:
                docu.pop(0)
                ord.pop(0)
        else:
            docu.append(docu[0])
            docu.pop(0)
            ord.append(ord[0])
            ord.pop(0)