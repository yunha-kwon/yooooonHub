nums = []

for i in range(9):
    a = int(input())
    nums.append(a)

max = 0

for i in nums:
    if i > max:
        max = i

print(max)
print(nums.index(max) + 1)