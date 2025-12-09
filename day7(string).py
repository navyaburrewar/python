# ########## string 

# #1
# ab ="hello"
# print(len(ab))


# ###2
# name="navyaburrewar"
# for ch in name:
#     print(ch)


#     #### 3
# name ="neha"
# for ch in name:
#     print(ch)

#     #### 4
#     ## checking a string contain  the specific word
# sentence="she is a good girl"
# word ="she"
# ab = "z"
# print(word in sentence)
# print(ab in sentence)

# ### 5
# ## upper case and lower case
# name ="navya"
# print(name.upper())
# print(name.lower())


# ### 6
# ## reversing a string using slicing
# name ="navyaburrewar"
# rev =name[::-1]
# print(rev)


# ## 8 
# ##r indexing 
# s="12345"
# print(s[3])
# print(s[0])


# ### slicing
# s="1234568"   ## slicing is based on the index
# ab=s[1:8]
# print(ab)
# mn =s[3:8]
# print(mn)


#  ## 9
# ### concadination
# a ="navya"
# b = "burrewar"
# print( a+b)


# ##10
# ##another way of concadiantion(appending)
# m="hello"
# m +="world"
# print(m)

# n="navya"
# n +="burrewar"
# print(n)



##11
### replace
name = "bavya"
newname =  name.replace( "b","n")
print(newname)


name = "nehl"
newname = name.replace("l","a")
print(newname)


### 12
## replaing all the spaces in the sentence to the dashes
name = "navya burrewar bichkundha"
newname = name.replace( " "," -")
print(newname)


##13
### Remove leading and trailing spaces.
## which is nothing but removing spaces front and back side
#strip which is the key word to remove thw spaces starting and ending

name ="  sunitha burrewar  "
new= name.strip()
print(new)


## 14 
## concadination of the string without using the +
a= "nandhini"
b= "reddy"
print(" _".join([a,b]))


#3 15
## checking an string is an palindrome are not
name ="banana"
rev = name[::-1]
if(name == rev):
    print("it is an palindrome")
else:
    print("not an palindrome")


name ="baccab"
rev = name[::-1]
if(name == rev):
    print("it is an palindrome")
else:
    print("not an palindrome")


    ## 16
 ## counting no of vowels and consonants
az= "m" 
if (az=="a") or (az=="e") or (az=="i") or (az=="o") or(az=="u"):
    print(" printvowel")
else:
    print("consonant")    

