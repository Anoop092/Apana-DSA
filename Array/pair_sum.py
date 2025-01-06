# given array in sorted order find the pair of elements in which the addition pair sum is equal to target sum

arr= [2,7,11,15]
target_sum = 19

def brute_force(arr, target_sum):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if arr[i] + arr[j] == target_sum:
                return (arr[i],arr[j])
    return (-1,-1)
def optimal_approach(arr,target_sum):
    start = 0 
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == target_sum:
            return (arr[start],arr[end])
        elif arr[start] + arr[end] <target_sum:
            start += 1
        else:
            end -= 1
    return(-1,-1)

print(brute_force(arr,target_sum))
print(f"The optimal approach ans is: {optimal_approach(arr,target_sum)}")
            