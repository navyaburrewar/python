##  Sum of First N Natural Numbers
## Find the sum of numbers from 1 to n using recursion.   
def sum(n):
    if n==0:
       return n
    else:
        return n+sum(n-1)

print(sum(30))    