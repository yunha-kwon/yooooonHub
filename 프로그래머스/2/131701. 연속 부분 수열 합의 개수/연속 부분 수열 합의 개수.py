from collections import deque

def solution(elements):
    ans = set()
    
    dq = deque(elements)
    
    for _ in range(len(dq)):
        sum = 0
        for i in dq:
            sum += i
            ans.add(sum)
                
        dq.append(dq.popleft())

    return len(ans)