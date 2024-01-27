n = int(input())
total_cnt = 0

for i in range(n):
    word = input()
    cnt = 0
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if new_word.count(word[j]) > 0:
                cnt += 1

    if cnt == 0:
        total_cnt += 1

print(total_cnt)