# Kristine Joy Barrina #BSCPE 1-5 # April 2, 2023
# Creating a program that decrypts a code

# PSEUDOCODE

# initialize python modules

from pyfiglet import Figlet
from termcolor import colored
from colorama import Style, Back
from tkinter import *

# Print a notice message that the program will decrypt a code
# Style the texts using pyfiglet
notice_message = Figlet (font = "standard")

# Style the texts using colorama
print (colored (notice_message.renderText("DECRYPT IT!"), "yellow"))


# Let the user input a string
user_input = str (input ( Back.WHITE + "\033[1m" + "Input a string:" + Style.RESET_ALL + " "))

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