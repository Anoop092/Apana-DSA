# Compute the exponantial of given number where time comploxity should be less than O(n)

exp = -5 
x = 3
ans = 1

if exp <  0:
    x = 1/x
    exp *= -1

while exp > 0:
    if exp % 2 == 1:
        ans = ans * x
    x = x*x
    exp = int(exp/2)

