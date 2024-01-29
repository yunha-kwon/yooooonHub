input1 = map(str, input())
input_lst = list(input1)

ans_lst = []

for i in input_lst:
    if 65 <= ord(i) <= 67:
        ans_lst.append(3)
    elif 68 <= ord(i) <= 70:
        ans_lst.append(4)
    elif 71 <= ord(i) <= 73:
        ans_lst.append(5)
    elif 74 <= ord(i) <= 76:
        ans_lst.append(6)
    elif 77 <= ord(i) <= 79:
        ans_lst.append(7)
    elif 80 <= ord(i) <= 83:
        ans_lst.append(8)
    elif 84 <= ord(i) <= 86:
        ans_lst.append(9)
    elif 87 <= ord(i) <= 90:
        ans_lst.append(10)

cnt = 0
for i in ans_lst:
    cnt += i
print(cnt)