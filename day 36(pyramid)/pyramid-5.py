## half star pyramid

n=5
for i in range(n):
    for j in range(i+1):
        print(i+1,end="")
    print()    


## full star pyramid 

n=6
num=1
for i in range(n):
    for j in range(i+1):
        print(" "*(n-i)+(2*i-1))

    
