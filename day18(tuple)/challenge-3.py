## challenge -3

## 1
## second largest no
t =(20,30,13,50)
e=list(t)
e.sort()
print(e[-2])


## 2
## sorting tuple based on 2nd element
t=((2,1),(4,3),(5,2))
soretd_tuple =tuple(sorted(t, key=lambda t: t[1]))
print(soretd_tuple)