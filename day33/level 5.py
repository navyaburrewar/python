## 26 Print an inverted triangle aligned left
for i in range(5):
    print("*"*i)



## 27   Print a reversed right triangle
n=5
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)


## 28 print an reversed right triangle
n=5
for i in range(0,n):
    print(" "*(n-i)+"*"*i)    




## 29   Print an inverted triangle using numbers
n=5
for i in range(n,0,-1):
    for j in range(1,1+i):
        print(j, end="")
    print()



    