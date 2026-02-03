## fibonacci sequence
#he Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:
## we will do this by the fibonacci sequence

def fabonoci(n):
    if n<=1:
        return n
    else :
        return fabonoci(n-1)+fabonoci(n-2)
print(fabonoci(8))



def fobonaic(m):
    if m<=1:
        return m
    else:
        return fabonoci(m-1)+fabonoci(m-2)
print(fabonoci(10))    


