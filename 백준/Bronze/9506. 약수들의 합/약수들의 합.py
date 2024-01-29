while True:
    N = int(input())
    if N == -1:
        break

    sum_lst = []
    sum_result = 0

    for i in range(1, N):
        if N % i == 0:
            sum_lst.append(i)

    for j in sum_lst:
        sum_result += j

    if sum_result == N:
        print(f'{N} = {" + ".join(map(str, sum_lst))}')
    else:
        print(f'{N} is NOT perfect.')