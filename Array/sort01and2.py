# sort 0,1,& 2 in given array

arr = [2,0,2,1,1,0,1,2,0,0]

mid, low, high = 0,0,len(arr) -1

while mid <= high:
    if arr[mid] == 0:
        arr[low] , arr[mid] = arr[mid],arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[high] , arr[mid] = arr[mid] , arr[high]
        high -= 1

print(arr)
