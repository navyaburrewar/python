## set mathematical operations methods

## 1 union
a={1,2,3}
b={2,3,5,7}

x=a.union(b)
print(x)


## intersection()
## common elements
y=a.intersection(b)
print(y)


## differences
z = a.difference(b)
print(z)
w =b.difference(a)
print(w)

### symmetric difference()
## removes common elements // returns not common elements
print(a.symmetric_difference(b))