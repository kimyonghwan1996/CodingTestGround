import itertools

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
a = 0

for i in range(n):
    a = max((nums[i] + nums[2*n-1-i]),a)

print(a)
