##level-3


## 21  Print a triangle of height 4 
for i in range(5):
    print("*"*i)


## 22   Print a triangle where last row has 10 stars

for i in range(11):
    print("*"*i)



##  23  Print an inverted triangle with

for i in range(5,0,-1):
    print("*"*i)



## 24   Print an inverted triangle of height 5

for i in range(6,0,-1):
    print("*"*i)


## 25    Print an inverted triangle using user input
n =int(input())
for i in range(n):
    print("*"*i)




## 26 Print an inverted triangle using $
for i in range(5):
    print("$"*i)




##   27  Print a triangle from 6 stars to 1 star
for i  in range(6,0,-1):
    print("*"*i)



## 28  Print an inverted triangle with fixed width

width = 10

for i in range(width, 0, -1):
    spaces = width - i
    stars = i
    print(" " * spaces + "*" * stars)

