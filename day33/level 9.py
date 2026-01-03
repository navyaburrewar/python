## 35  Print a triangle using odd numbers
n=3
num=1
for i in range(0,n+1):
    for j in range(i):
        print(num,end="")
        num+=2
    print()    