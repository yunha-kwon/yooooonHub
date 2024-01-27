word_lst = []
for i in range(5):
    word_lst.append(list(input()))
#print(word_lst)

for j in range(15):
    for i in range(5):
        if j < len(word_lst[i]):
            print(word_lst[i][j],end='')