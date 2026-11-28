n = int(input())
nums = list(map(int, input().split()))
sorted(nums)
for i in sorted(nums):
    print(i, end=" ")
nums.sort(reverse=True)
print()
for i in nums:
    print(i, end=" ")
# print(i for i in nums, end=" ")
# print(" ".join(nums.sort()))
# Please write your code here.
