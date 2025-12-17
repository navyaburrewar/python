num =[10,20,30,40,11]
print(sorted(num))


## 2nd method
n =[90,80,70,600]
n.sort()
print(n)


## second largest number
num =[10,20,40,50,70]         ## 3steps  
num =list(set(num))           ## 1. remove duplicates
num.sort()                    ## 2.sort
print(num[-2])                ## 3 .pic second element

