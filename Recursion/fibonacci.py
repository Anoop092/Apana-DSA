# find the nth term in fibonaci series


#using for loop

first_term, second_term = 0 , 1
n = 6

for i in range(2,n+1):
    ans = first_term + second_term 
    first_term = second_term
    second_term = ans

print(ans)

# using reccursion 
def fib(n):
    # base cases
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    return fib(n-1) + fib(n-2)

print(fib(6))