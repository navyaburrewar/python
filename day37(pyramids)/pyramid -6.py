
n=6
for i in range(0,n):
    print(" "*(n-i)+"*"*(2*i-1))


n=6
for i in range(0,n):
    print(" "*(n-i)+"*"*(2*i-1))



n=4
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,1+i):
     print(j,end="")
    for j in range(i-1,0,-1):
     print(j,end="")    
    print()
