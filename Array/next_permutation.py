# Find the Next permutation 

nums = [1,2,3,6,5,4]

#Find the pivot
pivot_index = -1
for i in range(len(nums)-2,-1,-1):
    if nums[i] < nums[i + 1]:
        pivot_index = i
        break

def reverse(nums,start=0,end = len(nums) - 1):
    while start <= end:
        nums[start] ,nums[end] = nums[end] , nums[start]
        start += 1
        end -= 1
    

# if pivot doesnot exist then return reverse the given array
if pivot_index == -1:
    reverse(nums)

# Find the right most element which is greater than pivot number
for i in range(len(nums)- 1, pivot_index - 1,-1):
    if nums[pivot_index] < nums[i]:
        nums[pivot_index] , nums[i] = nums[i] , nums[pivot_index]
        break

# Reverse the pivot+ 1 index to len(arr) - 1
reverse(nums,pivot_index + 1)

print(nums)
