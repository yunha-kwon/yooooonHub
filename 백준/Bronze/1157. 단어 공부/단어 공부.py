n = str(input())
upper_n = n.upper()

alpha_lst = list(upper_n)
alpha_set = list(set(alpha_lst))

alpha_cnt = []
for i in range(len(alpha_set)):
    alpha_cnt.append(alpha_lst.count(alpha_set[i]))

if alpha_cnt.count(max(alpha_cnt)) >= 2:
    print("?")
else:
    print(alpha_set[alpha_cnt.index(max(alpha_cnt))])