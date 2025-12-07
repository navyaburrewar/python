a=10
print(a)

###2

a,b,c=(1,3,4)
print(a,b,c)


##3  same variable as multiple values
a =(1,2,3)
print(a)


####4 same different variaable cant have same values
###a,b,c=(1)
###print(a,b,c)

###55  variable having same values 
a=b=c=22
print(a)



####
#1.start with alphabets
#2not start with  number symbol
# we can start with __
##it is case sensitive

####666
## to find addresess


a=3
print(id(a))

###777
#case sensitive

Python =12
python=10
print(Python)

##8
##addition oh two numbers
# all other arithmetic opereation

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

##9
##print length
name="navya"
print(len(name))


###10
#3type of data
name="navya burreawr"
age=20
print(type(name))
print(type(age))


##11
##SWAP 
x=10
y=20
x,y=y,x
print(x,y)

#12
##concadinate or combine
first ="hello"
second="world"
print(first+second)

##13
###using variable inside print
name="Navya"
print("my name is "+name)

#14
###increment the values
num=0
num=num+1
print(num)


##15
##decrement the values
n=100
n=n-1
print(n)


##16
#converting variable type
b="20"
b=int(b)
print(b)

## int to float
c=30
c=float(c)
print(c)

## 
num=120
digist=str(num)
print(f' "{digist}"')          
 ### here the f'"{digist}" formayed string which will write the code insidde the brackets into the string formate
 

 ##17
 ## rounding values
num=23.30
print(round(num))

##18
##deleting
num=100
print(num)
del(num)
## again printing of num we will get the error beacuse it deleted

##19
##user input

name =int(input())
print(name)


##20
##add two numbers using the user inputs
A =int(input())
B =int(input())
sum =A+B
print(sum)








