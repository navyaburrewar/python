## using dict()
d=dict(small=20,big=40)
print(d)

## accessing dict values:
marks ={
    "navya" :10,
    "pandu":20,
    "vivek":40
}
print(marks["navya"])


#ex -2
rollno={
     20:20,
     40:40,
     50:50
    
}
print(rollno[20])


## 5
## accessing using get() (safe way)
marks ={
    "navya" :10,
    "pandu":20,        ## if key is not pressent it will gives error
    "vivek":40
}
print(marks.get("navya"))

##6
## get()

files={
    "nandhu":20,
    "bindhu":40,        ##3 using get that if the key is not found it will gives none
    "neha":45

}
print(files.get("neha"))




