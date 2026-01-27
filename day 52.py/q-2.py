# Define a function
def square_number(number):
    result = number * number
    return result

# Take input from user
num = float(input("Enter a number: "))

# Call the function
output = square_number(num)

# Display result
print("The square of", num, "is", output)
