'''
    Lesson: If and Else
    Author: Mr. Kalisz
    Date Created: October 15, 2024
    Date Last Modified: October15, 2024
'''

#If review

num = 25

if num < 20: #Run when the boolean is true
    #Code inside the if state needs to be indented
    print("Number was less than 20")

#Else Statements

num = 25

#Only one of these can run at a time

if num < 20:
    print("If is true")
else: #Has no condition -> not (num < 20) -> num >= 20
    print("else statement ran")

if num < 15 and num > 5:
    print()
# num = 5 #No unindented code between if and else
else: # not (num < 15 and num > 5) -> num >= 15 or num <= 5
    print()
