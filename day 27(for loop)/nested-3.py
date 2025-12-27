for i in range(1,4):
    for j in range(1,4):
        print(f"i={i}, j={j}")

#What this line does

# print() → prints something to the console.
# f"i={i}, j={j}" → this is an f-string (formatted string literal) in Python.
# F-string meaning:
#The f before the quotes tells Python:
#“Replace any expressions inside {} with their current values.”
#{i} → replaced with the current value of i
#{j} → replaced with the current value of j
#So each time the loop runs, it prints the current combination of i and j.