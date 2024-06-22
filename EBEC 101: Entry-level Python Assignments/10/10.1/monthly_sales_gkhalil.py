"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 11/18/2022

Description:
    This program takes monthly data and plots the equivalent pie chart.

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
    months=['January','February','March','April','May','June','July','August','September','October','November','December'] #months of the year
    y=[] #list which will contain given monthly sales
    for i in range(12):
        y.append(int(input(f"Enter the sales for {months[i]}: "))) #for loop to gather sales for every month
    c = ('#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A') #desired colors from given
    ax.pie(y,colors=c,labels=months,) #labels can be set to the months list
    ax.set_title('Monthly Sales Values') #plot title
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
