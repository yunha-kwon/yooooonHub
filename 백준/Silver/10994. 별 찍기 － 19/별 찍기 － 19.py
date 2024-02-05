N = int(input())
star = [[' ' for _ in range(4*N-3)] for _ in range(4*N-3)]

def stars(n, x, y):
    if n == 1:
        star[y][x] = "*"
        return

    leng = 4*n-3

    for i in range(leng):
        star[y][x+i] = "*"
        star[y+i][x] = "*"
        star[y+leng-1][x+i] = "*"
        star[y+i][x+leng-1] = "*"

    stars(n-1, x+2, y+2)

stars(N,0,0)
for s in star:
    print(''.join(s))