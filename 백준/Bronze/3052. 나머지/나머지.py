num_lst = []

for i in range(10):
    a = int(input())
    num_lst.append(a % 42)

print(len(set(num_lst)))