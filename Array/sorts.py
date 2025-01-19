nums = [4,1,5,2,3]
nums_2 = [1,2,3,4,5]


def bubble_sort(nums):

    for i in range(0,len(nums)):
        is_swap = False
        for j in range(0, len(nums) - i -1):
            if nums[j] > nums[j+1]:
                is_swap = True
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
        if (not is_swap):
            break
    return nums
        
def selection_sort(nums):
    for i in range(0,len(nums)):
        smallest_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_index]:
                smallest_index = j
        temp = nums[smallest_index]
        nums[smallest_index] = nums[i]
        nums[i] = temp
    return nums
# print(bubble_sort(nums))
print(selection_sort(nums))
