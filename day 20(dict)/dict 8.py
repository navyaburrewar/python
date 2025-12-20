## looprs in the dictiory

## 1
## loops using key
marks ={
    "navya" :10,
    "pandu":20,        
    "vivek":40
}
for key in marks:
    print(key)


    ## 2
    ## loops using values
for value in marks.values():
 print(value)


 ##  3
 ## loops using both values nad keys in dict
 for keys,value in marks.items():
    print(keys,value)
