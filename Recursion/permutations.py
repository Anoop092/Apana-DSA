# find all the permutations in given array

arr = [1,2,3]
result = []
ds = []
frequency = [False for i in range(0,len(arr))]

def find_permutations(arr,ds,frequency,result):
    if len(arr) == len(ds):
        result.append(ds.copy())
        return
    for i in range(0,len(arr)):
        if not frequency[i]:
            frequency[i] = True
            ds.append(arr[i])
            find_permutations(arr,ds,frequency,result)
            ds.pop()
            frequency[i] = False
find_permutations(arr,ds,frequency,result)
print(result)