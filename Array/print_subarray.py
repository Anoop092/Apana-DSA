# Find all subarrays in give array

arr = [1,2,3,4,5,6,7]
arr_2 = [2,3,4,5,6,7]

for start_index in range(0,len(arr)):
    for end_index in range(start_index,len(arr)):
        for i in range(start_index, end_index + 1):
            print(arr[i],end="")
        print(end=',')
    print()
