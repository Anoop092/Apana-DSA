# Print all subsets of array

arr = [1,2,3]
ans = []
result = []

def subsets(arr,ans,index = 0):
    if index == len(arr):
        # Note we can't directly append a array if we append we are appending the ans address 
        result.append(ans.copy())
        return
    
    subsets(arr,ans,index + 1)
    ans.append(arr[index])
    subsets(arr,ans,index+1)
    ans.pop()

# subsets(arr,ans)
# print(result)

# If array contains duplicates values 
arr = [1,2,2]
arr.sort()

def subset_duplicates(arr,ans,index = 0):
    if index == len(arr):
        result.append(ans.copy())
        return
    
    ans.append(arr[index])
    subset_duplicates(arr,ans,index+1)
    ans.pop()
    index = index + 1 
    # skip the reapting index
    while index < len(arr) and arr[index] == arr[index - 1]:
        index += 1
    subset_duplicates(arr,ans,index)

subset_duplicates(arr,ans)
print(result)