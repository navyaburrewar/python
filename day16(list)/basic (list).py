## basic level questions in lists

## 1
### what is list
# A list is an ordered, mutable collection used to store multiple values in a single variable.

a = [10, 20, 30]



## 2
## How is a list different from a tuple?

##List	                 Tuple

#Mutable (changeable)	Immutable (not changeable)
#Uses []	            Uses ()
#Slower              	Faster

#lst = [1, 2, 3]         #tpl = (1, 2, 3)



## 3
## crating a list of 5 integers
num =[1,2,3,4,5]
print(num)


## 4
## accessing last element 
## by using the negative indexing
n =[10,20,39,39]
print(n[: :-1])        ## for the reversing
print(n[-1])           ## for last indexing



## 5 
## append is nothing but adding
lst =[20,30,40,506]
lst.append(24)
print(lst)


### 6
## length of a list
lst =[20,30,40,80,60,70,80]
print(len(lst))


### 7
## can a list  store different data types  ans = yes
lst =["navya",90,9.8,True ]
print(lst)


## 8
## indexing

v =[20,22,33,44,55,66]
z=v.index(22)
print(z)


