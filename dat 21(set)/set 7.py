## methods 

## add()
## update()
## remove()
## discard()
## pop()
## clear()
## copy()

#1.add()
a ={1,2,3,4}
a.add(5)
print(a)
a.update({20})
print(a)
a.remove(4)
print(a)
a.discard(3)     ## remove and discard are quit similar that 
print(a)         ## when we use remove() if element is not found it will shows error
a.discard(10)    ## when we use discard () it will not show error
print(a)

#a={1,2,3,4}  is this method are set
w=a.pop()
print(w)             ## pop() will removes a random element
print(a)             ## remove ## discard will  both removes specific element
                     ## again discard will not type error 
## clear()
a.clear()
print(a)

## copy()
#Creates a shallow copy of the set.
s = {1, 2, 3}
new_set = s.copy()
print(new_set)  





