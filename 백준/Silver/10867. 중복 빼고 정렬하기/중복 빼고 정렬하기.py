# 중복 빼고 정렬하기
N = int(input())
num_lst = list(map(int, input().split()))

num_lst = list(set(num_lst))
num_lst.sort()

print(*num_lst)