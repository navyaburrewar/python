##stings
## 1
## remove duplicate values
## using set values
a= 23,23,4,78,98,45,70
print(set(a))

##2
##  removing dhuplicate charactors
name = "navyaburrewar"
print(set(name))



### 3
###finding largest word
sentence = "she is eating mango"
words= sentence.split()
large_word = max(words, key=len)
print(large_word)


###finding small word
sentence = "god shiva is more powerful"
word =sentence.split()
small_word = min(word , key=len) 
print(small_word)



#### 4
###  finding words according to the alphabetical order
sentence="she is a beautiful girl"
words=sentence.split()
first_alphabet=sorted(words)
print(first_alphabet)



### 5
## capitalizing the  title

sentence = " i am from nizamabad"
words =sentence.title()
print(words)


### 6
### another way of capitalizing the  first word of sentences
sentence = "i am from hyd"
print(sentence.capitalize())   ## only first word of first letter only becomes capital


## 7
sentence = "i am from nizamabad"
words =sentence.capitalize()
print(words)                        ## this is also same as about 
   


## 8
## without using the title
sentence ="am a good girl"
words=sentence.split()
result =" ".join(word.capitalize() for word in words)
print(result)


### 9 
# counting no of words in the string
sentence = "neha and navya both are sisters"
words =sentence.split()
count= len(words)
print(count)

### 10
sentence = "akhil works in the hcl "
words =sentence.split()
count= len(words)
print(count)


## 11
##Check if two strings are anagrams.
str1 ="listen"
str2 ="silent"
if sorted(str1)==sorted(str2):
    print("anagrams")
else:
    print("not an anagrams")


    ##12
str1 ="cat"
str2="bat"
if sorted(str1)==sorted(str2):
    print("anagrams")
else:
    print("not an anagrams")




