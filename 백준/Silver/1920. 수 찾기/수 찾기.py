import sys

input()
A = list(set(map(int, sys.stdin.readline().split())))
input()
B = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in B:
    if i in A:
        print(1)
    else:
        print(0)