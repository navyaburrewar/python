##3 Print alphabet pattern using user input

n=6
ch = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end =" ")
    print()    