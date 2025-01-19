#importing the random
import random
#using while loop for boolean value whether it is true or false
while True:
#take input from the user whether it may contain lower or upper case letter
    choice=input("Enter the choice:").lower()
#include if condition to check whether the choice is equal or not
    if choice=='y' :
#take die1 which performs 1 to 6 random throws
        die1=random.randint(1,6)
#take die2 which performs 1 to 6 random throws
        die2=random.randint(1,6)
#print the die1 and die2 random numbers when the two dices are thrown
        print(f"({die1},{die2})")
#And make sure that when the choice is equal to n print thanks for playing
    elif choice=='n':
        print("Thanks for playing")
#Using break keyword to terminate the loop
        break
    else:
#Use else to print invalid choice
        print("Invalid choice")