import sys
input = sys.stdin.readline

S = input().strip()

str_lst = []

for i in range(len(S)):
    for j in range(len(S)):
        str_lst.append(S[i:i+j])

print(len(set(str_lst)))