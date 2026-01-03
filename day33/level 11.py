##  Print a triangle with reverse numbers
n=5
num=20
for i in range(n,0,-1):
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()        