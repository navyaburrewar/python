### control statments in forloop
### break
### continue


## break
# exit loop immediately
for i in range(1,11):
     if  i==5:
          break
     print(i)
     i+=1


## continue     
## Skips the current iteration and moves to the next.
for i in range(1,10):
    if i==6:
         continue
    print(i)
    i=i+1


## else
for i in range(1,11):
     print(i)
     i+=1
else:
     print("no not b/w range")     


