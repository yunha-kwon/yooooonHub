num_lst = []
for i in range(5):
    num = input()
    num_lst.append(num)

sum = 0
for i in num_lst:
    sum += int(i)
print(int(sum/len(num_lst)))

num_lst.sort()
print(num_lst[2])