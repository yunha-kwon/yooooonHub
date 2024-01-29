str_input = str(input())
cnt = 1

for i in str_input:
    if i == ' ':
        cnt += 1
    
if str_input[-1] == ' ':
    cnt -= 1

if str_input[0] == ' ':
    cnt -= 1

print(cnt)