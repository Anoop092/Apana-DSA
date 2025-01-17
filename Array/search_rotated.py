# search in rotated given array
nums = [3,4,5,6,7,0,1,2]
target = 0

start , end = 0 , len(nums) - 1
while start <= end:
    mid = int(start + (end - start) / 2)
    if nums[mid]  == target:
        print(mid)
        break
    elif  nums[start] < nums[mid]:
        if nums[start] <= target <=  nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    else:
        if nums[mid] <= target <= nums[end]:
            start = mid + 1
        else:
            end = mid - 1