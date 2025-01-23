# Sort an array using recurrsion 

arr = [2,1,7,6,4,5,9]

def insert_element(arr,poped):
    if len(arr) == 0 or arr[len(arr) - 1] <= poped:
        arr.append(poped)
        return
    val = arr.pop()
    insert_element(arr,poped)
    arr.append(val)

def recurrsion_sort(arr):
    # Base case
    if len(arr) == 1:
        return
    
    temp = arr.pop()
    recurrsion_sort(arr)

    insert_element(arr,temp)

recurrsion_sort(arr)
print(arr)



    
