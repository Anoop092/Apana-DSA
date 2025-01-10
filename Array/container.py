# Find the conatiner with most water 

arr = [1,8,6,2,5,4,8,3,7]

def brute_force(arr):
    max_area = float("-inf")
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            # Remember the area of water is controled by small height wall
            height = min(arr[i],arr[j])
            width = j - i
            max_area = max(max_area,height * width)
    return max_area
def optimul(arr):
    max_area,left,right = float("-inf"), 0,len(arr) - 1
    while left < right:
        width = right - left
        height = min(arr[left], arr[right])
        max_area = max(max_area, width * height)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(optimul(arr))
