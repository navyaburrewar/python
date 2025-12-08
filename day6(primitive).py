 #########3 float
## 1
ab=39.6
print(ab)



## 2
##converting  int to float
ab=35
print(float(ab))



### 3
##converting float to int
ab=36.8
print(int(ab))


## 4
## adition of two float numbers
num1=30.5
num2=35.9
sum =num1+num2
print(sum)

## 5
## multipilcation of float numbers
num1=2.0
num2=8.5
product=num1*num2
print(product)


## 6
### arthimetic operations
num1=2.0
num2=3.5
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)


#### 7
##finding the type of the data
num1=9.0
print(type(num1))


### 8
## checking is 15.0 is equal to the 15
nm = 15.0
ab =15
print(nm==ab)

a=20
b=40
print(a==b)



### 9
##rounding the number
num =49.5
print(round(num))

num2=3.4678
print(round(num2))


### 10
### printing only integer value

ab=4.7
print(int(4.7))




### 11
## priting only decimal
mn =2.678
print(mn-int(mn))

###
price =40.8976
print(price-int(price))



### 12
## converting float into the string  value
nm = 49.9084
print(str(nm))
print(f' "{nm} "')


## 13
## converting string to float
name ="2037"
print(float(name))

### 14
### finding sum of the 3 float numbers
a = 1.1
b=2.2
c=3.2
sum =a+b+c
print(sum)


## 15
##printing absolute value
a=-30.7
print(abs(a))


## 16
## avg of floating numbers
n=20.0
m=49.8
p=30.3
avg = n+m+p/2
print(avg)



### 17
ab = 8.94729
print(round(ab , 1))
print(round(ab , 2))
print(round(ab , 3))


mn =0.264748
print(round(mn , 1))
print(round(mn, 2))
print(round(mn , 4))


## 18
## finding the area of the circle
pi =3.141
r= 7
area = pi*r**2               ### area formula = pi *r**2
print(area)


## 19
### converting temperature from celsius to fahrenheit
c=25
f =(c* 9/5)+32                   ## formula f=(c* 9/5)+32
print("fahrenheit" ,f)


### 20 
## converting from fahrenheit to celsius
f=67
c=(f-32)*5/9                   ## formula   c=(f-32)*5/9
print("celsius",c)


### 21
## selling by discount problem
price =200.3
discount =20.3
sp = price -(discount/100-price)    ## formula of sp =mp-(discount/100-mp)
print( "sp:",sp)                          # mp= market price




### 22
### finding speed value
distance =100
time =20 
speed = distance/time
print(speed)

## 23
### checking addition of two float nu,bers is float or not
a=90.3
b=93.1
print(a+b)


## 24
### counting numbers after decimL AND before decimal
num =20.3872
s=str(num)
before ,after =s.split('.')
print("digits before the decimal:", len(before))
print("digits before the decimal:", len(after))



















