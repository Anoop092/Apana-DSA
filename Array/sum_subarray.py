# Calculate the maximum sum of all subarray

arr = [3,-4,5,4,-1,7,-8]


def brute_force(arr):
    max_sum = float("-inf")
    for i in range(0,len(arr)):
        current_sum = 0
        for j in range(i,len(arr)):
            current_sum += arr[j]
            max_sum = max(current_sum,max_sum)
    return max_sum
print(brute_force(arr))

