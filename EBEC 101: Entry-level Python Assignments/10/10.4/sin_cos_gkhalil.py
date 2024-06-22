"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 11/20/2022

Description:
    This program uses matplotlib to draw a plot of sine and cosine from 0 to 2π on the same axes.

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
import matplotlib.pyplot as plt
import math

"""Write new functions below this line (starting with unit 4)."""

def main():
    fig, ax = plt.subplots()
    x = range(0,361) #in degrees, easier to work with
    y1=[]
    y2=[]
    for n in x:
        y1.append(math.sin(math.radians(n))) #converting to radians before calculating sine and cosine
        y2.append(math.cos(math.radians(n)))
    
    ax.plot(x,y1,color='r')
    ax.plot(x,y2,color='b')
    ax.set_xticks([90,180,270,360]) #x ticks as required
    ax.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']) #x tick labels as required
    ax.set_yticks([-1,1])

    #formatting graph such that x axis passes through y-intercept = 0
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
