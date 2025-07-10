from collections import deque

def solution(priorities, location):
    answer = 0
    seq = [i for i in range(len(priorities))]
    
    idx, q = deque(seq), deque(priorities)
    
    while q:
        mx = max(q)
        cur = q.popleft()
        i = idx.popleft()
        
        if cur != mx:
            q.append(cur)
            idx.append(i)
            
        else:
            answer += 1
            if i == location:
                return answer