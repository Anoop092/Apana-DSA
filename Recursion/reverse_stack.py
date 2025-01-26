# Reverse a given stack in 0(1) space

arr = [1,2,3,4,5]

def insert_element(arr,poped_element):
    if len(arr) == 0:
        arr.append(poped_element)
        return
    target =arr.pop()
    insert_element(arr,poped_element)
    arr.append(target)

def resverseStack(arr):
    if len(arr) == 1:
        return
    poped_element = arr.pop()
    resverseStack(arr)
    insert_element(arr, poped_element)
resverseStack(arr)
print(arr)