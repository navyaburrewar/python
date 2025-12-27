## for loop
## A for loop in Python is a control flow statement that allows you to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code for each item in that sequence.
#Think of it as: “Do this action for every item in the collection.”
##Unlike some other languages, Python’s for loop iterates directly over items rather than using a counter by default.


#3 syntax

## for variable in sequence:
  ##code block to execute


#variable → takes the value of each item in the sequence, one by one
#sequence → any iterable (list, tuple, string, range, etc.)
#code block → indented statements that run for each item




#Flow of Execution

#Take the first item from the sequence and assign it to the variable.
#Execute the loop body.
#Move to the next item in the sequence.
#Repeat until all items are processed.
#Exit the loop.


# ex-1
fruits=["apple","banana","cherry"]
for fruit in  fruits:
    print(fruit)