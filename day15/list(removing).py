## removing

## 1 remove()
## 2 pop()
## 3clear()
## 4del()

## remove

n =[10,20,40,50]
n.remove(10)
print(n)


b=["navya","choti", "neha"]
b.remove("neha")
print(b)



## pop
m =[20,30,50,70]
m.pop(0)
print(m)


k=["navya",10,10.4]
k.pop(1)
print(k)


k=["navya",10,10.4]
k.pop()           ## empty will remove the last element  ## index vice
print(k)





## delete

g = [ 20,30,40]
del g[1]             ## index vice it can be used for the slicing'
print(g)


f =[200,30,40,50]
del f[0:2]
print(f)


f =[200,30,40,50]           ## removing multiple elements
del f[1:2]
print(f)



f =[200,30,40,50,20,300,400]           ## removing multiple elements
del f[1:2]                               # 1 only slicing that one is removing
print(f)



r =[200,30,40,50,20,300,400]           ## removing multiple elements
del r[2:6]                               #  2,3,4,5 only slicing that one is removing
print(r)


## removing alternative numbers using the delete

n=[10,20,30,40]
del n[::2]
print(n)



n=[10,20,30,40,32,42,52,12,24]
del n[::3]                         ## to continues numbers and one element jump
print(n)


##@ clear
lst=[10,20,30,40]
lst.clear()                ## clear will remove all the elements
print(lst)