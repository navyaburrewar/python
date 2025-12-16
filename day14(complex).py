### complete complex numbers


## propertices
## immutable(cannot be changed)
##uses j (not i)    beacuse  we use the i for indicating the variables that so to avoid confusion
# j = square root of -1
 ## comparatipn is not allowed in complex numbers


## 1
#basic question 
x =3+8j
print(x)



## 2
## direct assignment
## x= 4+5j
x = complex(3,4)
print(x)



###3
## accessing real and imaginary parts
z =5 +10j
print(z.real)
print(z.imag)


##4
z =5 +10j
print(type(z))



### 5
a =2+4j
b = 3+6j
print(a+b)
print(a-b)
print(a*b)
print(a/b)

## 6
## complex numbers storing decimal values

a=2.4+6.7j
print(a)


## 7
##  creating a complex no using complex
z =complex(10,20)
print(z)

## 8
## complex numbers cannot use the comparision if it use we will get errors
#print(3+3j >3+49j)
          ##3 output is error


###9
z = complex(0,5)
print(z)

## 10
z=10
x=complex(z)
print(x)

## 11
## addition of two complex numbers
a = complex(3,20)
b = complex(2.30)
print(a+b)
            

### 12
## case sensitive
z =  20 +18J
print(z)


a =  20 +18j
print(a)

if z==a:
    print("equal")
else:
    print("not equal")
              
### 13
## complex number cannot be order
### beacause we will not use the comparision here
## >,<,=<,....


## internally represtation of python
#(real , complex)


### 14
 ## complex numbers can be used as the dictionary
d = {2+3j: "value"}
print(d)


## 15
## differnce b/w the math nad cmath
## maths is applicabale for the integers
## cmaths is applicable for the complex numbers
 

## 16
 ## for integers 
import  math
print(math.sqrt(16))



## 17
## for complex numbers
import cmath
print(cmath.sqrt(-10))



