## ## Write a python code to accept a string and count the number of vowels and consonants.

name= "navya burrewar"
vowels="aeiou"

vowel_count=0
consonants_count=0


for ch in name.lower():
    if ch in vowels:
     vowel_count+=1
    elif ch.isalpha:
      consonants_count+=1

print("vowels",vowel_count)
print("consonats",consonants_count)       
 


