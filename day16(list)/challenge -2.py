#   challeng  = 2

## 1
## sum of elements in the list
lst =[20,30,40,50]
print(sum(lst))



## 2
## remove the duplicate 
lst =[20,20,30,40,50,60]
result =[]
for i in lst :
 if i not in result:
    result.append(i)
print(result)    


## 3
## largest and smallest numbers
num =[20,20,10,24,90]
print(max(num))
print(min(num))

## 4
## reversing s list
a =[19,20,30,40]
s = a[: : -1]
print(s)


## 5
## count how mant times an element is repeating in the list
g =[10,20,30,40,50,60]
print(g.count(10))
print(g.count(140))

## 6
## checkin list is empty or not
lst =[]
if lst ==[]:
  print("list is empty")
else :
  print("not empty")


## 7
## merge of two lists
lst1 =[10,20,39]
lst2 =[23,40,50]
x = lst1 +lst2
print(x)


## 8
## sorting a list
lst=[10,20,30,405,60,70]
m=sorted(lst)
print(m)
x =m[: : -1]
print(x)


## 9
##another way of sorting
lst=[10,20,30,405,60,70]
lst.sort()
print(lst)

lst.sort(reverse=True) 
print(lst)



## 10
## find  vev n and odd 
k =[10,20,30,40,2,3,5]
even=[]
odd =[]
for i in k:
  if i % 2==0:
    even.append(i)
  else:
    odd.append(i)
print(even)
print(odd)


## 11
## slicing list
num=[10,20,30,40,50,607,]
print(num[1:4])