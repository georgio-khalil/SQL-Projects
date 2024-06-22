"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/08/2022

Description:
    This program returns the color of a specified pocket in a roulette wheel. If the number is invalid, returns invalid input. 

Contributors:

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():

    n = int(input("Please choose a pocket number: "))

    if n < 0 or n > 36: #if pocket number is too low or too high
        print ("  Invalid Input!")
    elif n == 0: #pocket 0
        color = 'green'
        print (f"  Pocket number {n} is {color}.")
    elif n < 11: #pockets 1 through 10
        if n % 2 == 0: #even-numbered pocket
            color = 'black'
            print (f"  Pocket number {n} is {color}.")
        else: #odd numbered pocket
            color = 'red'
            print (f"  Pocket number {n} is {color}.")
    elif n < 19: 
        if n % 2 == 0: 
            color = 'red'
            print (f"  Pocket number {n} is {color}.")
        else: 
            color = 'black'
            print (f"  Pocket number {n} is {color}.")
    elif n < 29: 
        if n % 2 == 0: 
            color = 'black'
            print (f"  Pocket number {n} is {color}.")
        else: 
            color = 'red'
            print (f"  Pocket number {n} is {color}.")
    else: 
        if n % 2 == 0: 
            color = 'red'
            print (f"  Pocket number {n} is {color}.")
        else: 
            color = 'black'
            print (f"  Pocket number {n} is {color}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
