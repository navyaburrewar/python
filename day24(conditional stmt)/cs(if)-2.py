##There are patterns where only if is used, without else or elif

#  1. Simple if pattern (most basic)
#Used when you want to do something only if a condition is true.
age =20
if age >= 18:
    print("Eligible to vote")


# 2  Guard condition pattern
#Used to protect code from running in wrong case


## without guard condition
# a = 10
# b = 0
# print(a / b)   ## error

## with guard condition
a = 10
b = 0

if b == 0:
    print("Division not possible")
    # program stops here
if(b!=0):
   print(a / b)   



## 3 Validation pattern
#Used to check input or data.
marks =101
if marks < 0 or marks > 100:
    print("Invalid marks")




## 4 Multiple independent if statements
# Each if is checked separately.if n % 2 == 0:
n=30
if n%2==0:
    print("Even")

if n > 0:
    print("Positive")



## 5   Flag-based if pattern
# Used when a boolean variable controls behavior.

# A flag is a variable that stores True or False
#   (also called a boolean variable).
#It acts like a switch:
#We use a flag to decide whether some code should run or not.
#True → ON
#False → OFF

#if flag:
    # code runs only when flag is True
    
    ab = True   # flag
if ab:
    print("Welcome User")

# ex-2
greeting= False

if greeting:
    print("Welcome User")   ## no ouput nothing happens


# Early-exit / return pattern (functions)
#Very important in exams & real code.


def check_number(n):
    if n < 0:
        return "Negative"
    return "Positive"
print(check_number(4))


# if with pass (placeholder pattern)

# Used when logic will be added later.
x=90 
if x > 10:
 pass

#important things

#Keyword          What it does
#pass	  ->       Does nothing
#print    ->     	 Shows output
#return	  ->       Sends value back
#break    ->     	 Stops loop
#continue ->	     Skips loop step