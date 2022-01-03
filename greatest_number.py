# Problem
# Write a program to print the greatest of 4 numbers entered by the user

# Solution
# Using the input function to define the numbers provided by the user
# THE VALUE IS DEFINED WITHIN STRINGS WHEN WE USE THE INPUT FUNCTION (We have to use the int() function to convert them into integers)
a = int(input("Enter the first number\n")) 
b = int(input("Enter the second number\n"))
c = int(input("Enter the third number\n"))
d = int(input("Enter the fourth number\n"))

if (a > d): # Checks if the first number is greater than the fourth number
    num1 = a # Storing the greater numbers in variables
else:
    num1 = d

if (b > c): # Checks if the second number is greater than the third number
    num2 = b
else: 
    num2 = c

if (num1 > num2): # Checks if num1 is greater than num2
# Printing the result
    print(f"{num1} is the greatest number") 
else:
    print(f"{num2} is the greatest number")
