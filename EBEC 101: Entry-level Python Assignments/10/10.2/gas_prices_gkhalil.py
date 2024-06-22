"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/18/2022

Description:
    This program reads the weekly gas price from a file and generates a plot from the data.

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

"""Write new functions below this line (starting with unit 4)."""

def main():
    fig, ax = plt.subplots()
    x=list(range(1,53))
    y=[] #list which will contain gas prices
    with open('2008_Weekly_Gas_Averages.txt') as fo: #context manager
        lines=fo.readlines() #split text into lines
        for string in lines:
            y.append(float(string)) #store weekly gas price as float in list y
    ax.plot(x,y)
    ax.set_title('2008 Weekly Gas Prices') #plot title
    ax.set_xlabel('Weeks (by number)') #x label
    ax.set_ylabel('Average Price (dollars/gallon)') #y label
    ax.grid() #enable gridlines
    ax.set_xlim(1,52)
    ax.set_ylim(1.5,4.25)
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
