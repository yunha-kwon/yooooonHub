vowels = ['a','e','i','o','u','A','E','I','O','U']

while True:
    cnt = 0
    s = input()
    if s == '#':
        break

    for i in s:
        if i in vowels:
            cnt += 1

    print(cnt)