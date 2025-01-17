# Find the peak element in mountain array
arr = [0,3,8,9,5,2]
# we know that peack index doesnot exist at first and lastindex of array
start , end = 1 , len(arr) - 2

while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        print(mid)
        break
    elif arr[mid] > arr[mid -1]:
        start = mid + 1
    else:
    
        end = mid - 1