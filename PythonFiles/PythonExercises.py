# Question 1
# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# Solution
# ---------------------------------------------------------------------------------
import datetime


def calculate_Area(radius):
    pi = 3.14
    return pi * (radius ** 2)
# Use input keyword to get a data from the user


radius_of_user = float(input("Enter a radius: "))

print(calculate_Area(radius_of_user))
print("\n\n\n")
# Question 2
# Write a Python program to display the current date and time.
# Solution
# ----------------------------------------------------------------------------------------

Current_datetime = datetime.datetime.now()
print("Current date and time : ")
print(Current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

# Explanatios
# The datetime module supplies classes for manipulating dates and times in both simple and complex ways. datetime.now(tz=None) returns the current local date and time. If optional argument tz is None or not specified, this is like today().
# date.strftime(format) returns a string representing the date, controlled by an explicit format string. Format codes referring to hours, minutes or seconds will see 0 values.
# The said code imports the "datetime" module, gets the current date and time, and finally prints it in a formatted string.
# 1. The first line import datetime imports the datetime module which supplies classes for manipulating dates and times.
# 2. The second line now = datetime.datetime.now() creates a datetime object for the current date and time.
# 3. The third line print ("Current date and time : ") prints the string "Current date and time : " to the console.
# 4. The fourth line print (now.strftime("%Y-%m-%d %H:%M:%S")) uses the strftime() method of the datetime object to format the date and time as a string in the format "YYYY-MM-DD HH:MM:SS" and prints it to the console.


# The strftime() method returns a string representing the date, controlled by an explicit format string. The format codes used in this example are:
# 1. %Y: year with century as a decimal number.
# 2. %m: month as a zero-padded decimal number.
# 3. %d: day of the month as a zero-padded decimal number.
# 4. %H: hour (24-hour clock) as a zero-padded decimal number.
# 5. %M: minute as a zero-padded decimal number.
# 6. %S: second as a zero-padded decimal number.

# Question 3
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# Solution---------------------------------------------------------------------------------------------------------------


for x in range(1500, 2700):
    if x % 7 == 0 and x % 5 == 0:
        print(x)


# Question 4
# Write a Python program to guess a number between 1 to 9
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess,
# user will get a "Well guessed!" message, and the program will exit.
# Solution

number = int(
    input("\n\nEnter a number to guess whether this number between 1 to 9: "))

while not (number >= 1 and number <= 9):
    print("Enter a digit again!!!!!")
    number = int(
        input("\n\nEnter a number to guess whether this number between 1 to 9: "))

print("Well guessed!")
