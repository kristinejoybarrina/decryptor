# Kristine Joy Barrina #BSCPE 1-5 # April 2, 2023
# Creating a program that decrypts a code

# PSEUDOCODE

# Let the user input a string
user_input = str (input ("Input a string: "))

# Create a variable that has empty strings
output_str = ""

# Create a for loop with range of user's length input
for i in range (len(user_input)):

# Use if-elif-else to check each character written by the user


#   if "*" change to "a"
    if user_input [i] == "*":
        output_str += "a"

#   if "&" change to "e"
    elif user_input [i] == "&":
        output_str += "e"
        
#   if "#" change to "i"
    elif user_input [i] == "#":
        output_str += "i"   
    
#   if "+" change to "o"
    elif user_input [i] == "+":
        output_str += "o"
 
 #   if "!" change to "u"
    elif user_input [i] == "!":
        output_str += "u"
    
# If the character is not a punctuation then proceed to else
    else:
        output_str += user_input [i]

print (output_str)