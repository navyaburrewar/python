##  Print pattern using same alphabet per row

n=8
for i in range(n+1):
    for j in range(i+1):
        print(chr(65+i),end= " ")
    print()    