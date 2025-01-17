# Find the product of array except self

nums = [1,2,3,4]

prefix = [0 for i in range(len(nums))]
suffix = [0 for i in range(len(nums))]

prefix[0] = 1
suffix[len(nums) - 1] = 1

for i in range(1,len(nums)):
    prefix[i] = nums[i-1] * prefix[i-1]

for j in range(len(nums) - 1 - 1, -1, -1):
    suffix[j] = nums[j + 1] * suffix[j + 1]

ans = [prefix[i] * suffix[i] for i in range(0,len(nums))]
print(ans)