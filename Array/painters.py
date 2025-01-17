# Painter's partion problems

arr = [40,30,10,20]
no_of_boards = 4 
no_of_painters = 2

start,end = max(arr) , sum(arr)

def isValid(mid,arr,no_of_painters):
    painters = 1 
    no_of_boards_given = 0
    for boards in arr:
        if boards + no_of_boards_given <= mid:
            no_of_boards_given += boards
        else:
            no_of_boards_given = boards
            painters += 1
    return painters <= no_of_painters


while start <= end:
    mid = start + (end - start)//2
    if isValid(mid,arr,no_of_painters):
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
