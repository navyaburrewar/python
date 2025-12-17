##3 commmon element in two lists

num1=[20,30,40,50,60,70]
num2=[49,50,70,60,30,56]
common = list(set(num1) & set( num2))
print(common)