n = int(input())
num_input = int(input())

new_num = list(str(num_input))
sum = 0
for i in new_num:
    sum += int(i)

print(sum)