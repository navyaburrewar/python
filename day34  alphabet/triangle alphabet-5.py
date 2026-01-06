## Print alphabet square
for i in range(4):
    for j in range(4):
        print(chr(65+j), end=" ")
    print()    




## Print alphabet square
for i in range(4):
    for j in range(4):
        print(chr(65+i), end=" ")
    print()        




n=4
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()        