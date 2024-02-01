import sys
def binarySearch(key, my_card, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if key == my_card[mid]:
        return my_card[start:end+1].count(key)

    elif key < my_card[mid]:
        return binarySearch(key, my_card, start, mid-1)

    else:
        return binarySearch(key, my_card, mid+1, end)

N = int(sys.stdin.readline())
my_card = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
check_card = list(map(int, sys.stdin.readline().split()))

result_dic = {}
for i in my_card:
    start = 0
    end = len(my_card) - 1
    if i not in result_dic:
        result_dic[i] = binarySearch(i, my_card, start, end)

print(' '.join(str(result_dic[x]) if x in result_dic else '0' for x in check_card))