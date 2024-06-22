"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/15/2022

Description:
    This program imports a custom module to draw a random string of vowels.

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels as v #imported module containing draw functions
import random as r

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    l = ['a','e','i','o','u']
    order = r.sample(l,5) #sample 5 items without replacement giving us the random order of vowels
    
    for i in order: #call corresponding draw function according to order list
        if i == 'a':
            v.draw_a()
        elif i == 'e':
            v.draw_e()
        elif i == 'i':
            v.draw_i()
        elif i == 'o':
            v.draw_o()
        elif i == 'u':
            v.draw_u()
        forward(20) #space between letters


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
