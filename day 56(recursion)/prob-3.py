## power of a number

def function(n,m):
    if m==0:
        return 1
    elif m==1:
       return n
    else:
        return n*function(n,m-1)
print(function(3,4))    
    


