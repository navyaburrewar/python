### challenge -3

##  1
## list comprehension  which is nothing but the 
##short & clean way to create lists using a single line of code

#syntax 
# [expression for item in iterable if condition]

# ex-1
## square of numbers
squares =[x*x for x in range(5)]
print(squares)   

## ex-2
## even number only
evennumber =[n %2 == 0  for n in range(10) ]
print(evennumber)

## ex-3
even =[x for x in range(10) if x%2==0]
print(even)

## ex-4
odd=[x for  x in range(10) if x%2==1]
print(odd)


## ex -5 
## converting string to upperclass
name = ["navyaburrewar"]
upper=[character.upper() for character in name]
print(upper)

