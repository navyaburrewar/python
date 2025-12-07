### data types

###arithmetic operations
#1
a=2
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)


####integer division####
###2
print(20//5)     ##coefficiant value
a=100
b=5
print(a//b)



####  To get remainder values we have to use "%"- module operation
###3
print(50%10)
print(50%4)
print(100%3)
print(45%6)

#### 4
print(2**5)


#### 5
a= 15,29,18
print(max(a))    ### large/max number
print(max(a))    ### small/min number


## 6
##checking   even or odd
num =27
if num%2==1:
  print( "odd number")  
else :
  print("even number")

###7 
##square
print(14**2)
print(20**2)

##8
##sum of integers 1 to 10
## using range concept
for i in range(1,11):
  print(i)


### 9
# printing absolute value nothing but positive value
num =-70
print(abs(num))
print(abs(-100))
print(abs(-200))

## 10
###factorial of an number
num =4
fact=1
for i in range(1,num+1):
  fact=fact*i
  print(fact)


#### 11
  num=5
  fact=1
  for i in range (1,num+1):
    fact=fact*i
    print(fact)



###### 12
### priting length
ab=1234560
length=len(str(ab))
print(length)


xy="navyaburrewar"
lenth=len(str(xy))
print(lenth)



ab=8106809341
lenth=len(str(ab))
print(lenth)



##  13
#### position  of the value

nm = "nandhini reddy"
print(nm[0])
print(nm[9])
print(nm[10])




#### 14
### reversing the string
id =234567
rev=int(str(id)[::-1])
print(rev)


name ="navyaburrewar"
rev=str(name[::-1])
print(rev)


abc ="nikhil"
rev=str(abc[::-1])
print(rev)

number=8106809341
rev = int(str(number)[::-1])
print(rev)



##### 15
## palindrome
num=121
rev =int(str(num)[::-1])
if (num==rev):
  print("palindrome")
else:
  print("not palindrome")



  name ="NAVYA"
  rev=(str(name)[::-1])
if(name==rev):
  print("palindrome")

else:
 print("not an palindrome")


 









