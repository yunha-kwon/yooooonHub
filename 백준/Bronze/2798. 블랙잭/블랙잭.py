N, M = map(int, input().split())
card_input = list(input().split())

sum = 0

sum_lst = []

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and i != k:
                sum_lst.append(int(card_input[i]) + int(card_input[j]) + int(card_input[k]))

possible_num_lst = []

for i in set(sum_lst):
    if i <= M:
        possible_num_lst.append(i)

print(max(possible_num_lst))