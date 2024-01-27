word_lst = []

for i in range(5):
    word_lst.append(list(input()))

for i in range(15):
    for j in range(5):
        if i < len(word_lst[j]):
            print(word_lst[j][i], end='')