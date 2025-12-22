## update methods // (modify originsl methods sets0)
n ={10,30,40,50}
m ={80,39,58,60}


## union
n|=m            # |= works like n = n.union(m)
print(n)     

## intersection
n&=(m)         # &= works like n= n.intersection(m)
print(n)

## difference
n-=(m)
print(n)       # -= works like n = n.difference(m)


# ##Symmetric Difference 
n^=(m)                    # ^= works like n = n.difference(m)
print(n)