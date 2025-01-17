# Find the minimum possible maximum page

books = [2,1,3,4]
n = 4 
m = 2

start = 0
end = sum(books)

def isValid(mid,books,m):
    pages = 0 
    students = 1
    for page in books:
        if page > mid:
            return False
        if page + pages <= mid:
            pages = page + pages
        else:
            pages = page
            students += 1
    return students <= m



while start <= end:
    mid = start + (end - start)//2
    if isValid(mid,books,m):
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)
    
