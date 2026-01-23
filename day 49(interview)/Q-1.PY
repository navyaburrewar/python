# ##Write a program to solve a classic ancient Chinese puzzle: 
# # We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# #  How many rabbits and how many chickens do we have?

# #Hint: Use for loop to iterate all possible solutions.


heads=35
legs=94
for chiken in range(36):
    rabbits=heads-chiken
    if 2*chiken+4*rabbits==legs:
      print("chiken",chiken)
      print("rabbit",rabbits)