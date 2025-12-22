## update methods // (modify originsl methods sets0)
n ={10,30,40,50}
m ={80,39,58,60}


## union
n|=m            # |= works like A = A.union(B)
print(n)     

## intersection
n&=(m)         # &= works like A = A.intersection({2,3})
print(n)

## difference
n-=(m)
print(n)       # -= works like A = A.difference({3})


# ##Symmetric Difference 
n^=(m)
print(n)