#challenge-2

## 1
## convert list to tuple
list =[10,30,50]
print(tuple(list))


## 2
## sum of elements in tuple
t =(1,3,4,68)
print(sum(t))

## 3
## counting an occurrences of an element
t =(12,23,34,45,12)
print(t.count(12))


## 4
## index of an element
a=(10,20,304,96)
print(a.index(20))

### 5
##reverse of an element
n =(23,49,50,37)
print(n[::-1])


## 6
# check if an element exists in tuple
t =(20,39,49)
if 49 in t:
    print("exists")
else:
    print("not")

## 7
## unpack  a tuple into variable
t =(1,2,3)
a,b,c =t
print(a,b,c)   # each element is assigned to a variable


## 8
## accessing elements in neasted tuple
t =(12,23,45,(34,56,67))
print(t[3][0])


## 9
##merge to tuples
t1=(12,23,45)
t2=(24,65,98)
print(t1+t2)


## 10
## removing duplicates from a tuple
t =(10,20,30,10,10)
unique =tuple(set(t))
print(unique)

