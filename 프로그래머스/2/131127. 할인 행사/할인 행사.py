def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9): # i = 0, 1, 2, 3, 4
        ten_items = discount[i:i+10] # 0~9 / 1~10 / 2~11 / 3~12 / 4~13 (10개씩 자른거)
        
        cnt = [0] * len(want) # [0, 0, 0, 0, 0]
        for item in ten_items:
            for j in range(len(want)):
                if item == want[j]:
                    cnt[j] += 1
        
        if number == cnt:
            answer += 1
    
    return answer