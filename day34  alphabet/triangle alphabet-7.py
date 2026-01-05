## Print continuous alphabet triangle
n=6
ch=66
for i in range(n):
    for j in range(i+1):
        print(chr(ch),end =" ")
        ch+=1
    print()    