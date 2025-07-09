def solution(n):
    if n < 3:
        return n
    
    fibo = [0] * (n+1)
    fibo[1] = 1
    fibo[2] = 2
    
    for i in range(3, n+1):
        fibo[i] = fibo[i-2] + fibo[i-1]
    
    return fibo[n] % 1234567