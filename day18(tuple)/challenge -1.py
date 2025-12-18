##  challenge -1

## 1
# what is an tuple  ?

# A tuple is a collection of ordered elements in Python that is immutable (cannot be changed after creation).
#Tuples are written using parentheses ()


### 2
#Difference between list and tuple

#Feature   	  List	          Tuple
#Syntax	      [ ]	                  ( )
#Mutability	  Mutable 	        Immutable (cannot be changed)
#Performance  Slower	         Faster
#Use case	   data changes	    data should not change



## 3
## creating a tuple
t1 =(1,2,3)
t2=("navya",20)
t3=()
print(t1)
print(t2)
print(t3)


## 4
#Why is (5,) a tuple but (5) is not?

# ans
#(5) is treated as an integer, not a tuple.
#The comma , defines a tuple.
type((5))    # int
type((5,))   # tuple

### 5 accessing of elements
t =(1,2,3,4)
print(t[1])
print(t[-1])

## 6  can tuple store different values 
#3 ans : yes
t =(1,"navya",10,12.3, True)
print(t)

## 7 what happen if we try to modify a tuple
#3 ans : type error beacuse tuple cannot be modifyed
#TypeError: 'tuple' object does not support item assignment


## 8 length
t =(20,30,40,50,10)
print(len(t))

## 9 loop in tuple
t=(1,2,3,4,5)
for i in t:
 print(i)

 ## 10 max and min elements
 t=(10,20,30,40,50)
 print(max(t))
 print(min(t))