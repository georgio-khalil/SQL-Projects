"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 06.4 - Log Spiral
Date: 10/15/2022

Description:
    This program draws a logarithmic spiral using turtle commands.

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
from turtle import *
import math as m


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    #setting up parameters
    a=4
    b=0.22
    penup()
    for theta in range (1081): #number of iterations by trial and error
        goto(a*m.exp(b*m.radians(theta))*m.cos(m.radians(theta)),a*m.exp(b*m.radians(theta))*m.sin(m.radians(theta)))
        pendown()#to avoid drawing from 0,0 to first point
        #assign x and y coordinates using goto function. x and y are according to the given formula
"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
