# Kristine Joy Barrina #BSCPE 1-5 # April 2, 2023
# Creating a program that decrypts a code

# PSEUDOCODE

# Let the user input a string
user_input = str (input ("Input a string: "))

# Create a variable that has empty strings
output_str = ""

# Create a for loop with range of user's length input
for i in range (len(user_input)):

# Use if-else to check each character written by the user


#   if "*" change to "a"
    if user_input [i] == "*":
        output_str += "a"

    
# If the character is not a punctuation then proceed to else
    else:
        output_str += user_input [i]

print (output_str)