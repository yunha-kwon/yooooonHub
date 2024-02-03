import sys
input = sys.stdin.readline

A, B = map(int, input().split())

num_A = list(map(int, input().split()))
num_A = set(num_A)
num_B = list(map(int, input().split()))
num_B = set(num_B)

print(len((num_A - num_B) | (num_B - num_A)))