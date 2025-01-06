# Find majority element where frequency is greater than n/2 give that majority elements always exist
arr= [2,2,1,1,1,2,2,2]

def brute_force(arr):
    for i  in range(0,len(arr)):
        ans=arr[i]
        freq = 0
        for j in range(0,len(arr)):
            if ans == arr[j]:
                freq += 1
        if freq > int(len(arr)/2):
            return ans
        
def optimul_approach(arr):
    arr.sort()
    freq = 1
    ans = arr[0]
    for i in range(1,len(arr)):
        if ans ==arr[i]:
            freq += 1
        else :
            freq = 1
            ans = arr[i]
    if freq > int(len(arr)/2):
        return ans
    
def mores(arr):
    freq = 0
    ans = 0
    for i in range(0,len(arr)):
        if freq == 0:
            ans = arr[i]
        if ans == arr[i]:
            freq += 1
        else:
            freq -= 1
    return ans
    






print(brute_force(arr))
print(mores(arr))
print(optimul_approach(arr))