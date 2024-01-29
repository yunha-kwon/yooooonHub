chess_input = map(int, input().split())
chess_lst = list(chess_input)

answer_lst = [1, 1, 2, 2, 2, 8]

lst = []

for i in range(6):
    lst.append(answer_lst[i] - chess_lst[i])

print(*lst)