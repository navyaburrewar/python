# Print a triangle using even numbers
n=4
num=0
for i in range(0,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=2
    print()    