def solution(k, tangerine):
    # [1, 3, 2, 5, 4, 5, 2, 3] 이면 {1: 1개, 2: 2개, 3: 2개, 4: 1개, 5: 2개}
    dic = {}
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    
    # {1: 1개, 2: 2개, 3: 2개, 4: 1개, 5: 2개} 면 values 기준 내림차순 정렬
    sorted_val = sorted(dic.values(), reverse=True) # [2, 2, 2, 1, 1]
    
    cnt = 0 # 귤의 총 개수
    type_cnt = 0 # 귤 크기 종류의 개수
    # k개 선택
    for i in sorted_val: # i = 2, 2, 2, 1, 1
        cnt += i
        type_cnt += 1
        if cnt >= k:
            break
    
    return type_cnt