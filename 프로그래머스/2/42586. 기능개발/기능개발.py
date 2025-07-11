from collections import deque

def solution(progresses, speeds):
    answer = []
    
    pro_q = deque(progresses)
    spe_q = deque(speeds)
    
    while pro_q:
        
        for i in range(len(pro_q)):
            pro_q[i] += spe_q[i]
        
        task = 0
        while pro_q and pro_q[0] >= 100:
            pro_q.popleft()
            spe_q.popleft()
            task += 1
        
        if task != 0:
            answer.append(task)

    return answer