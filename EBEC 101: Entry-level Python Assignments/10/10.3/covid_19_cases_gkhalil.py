"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 11/18/2022

Description:
    This program reads covid-19 data from a file and generates a plot of cumulative new cases.

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
import datetime

"""Write new functions below this line (starting with unit 4)."""

def main():
    fig, ax = plt.subplots()
    dates=[]
    x=[] #list which will contain weekly start date
    y=[] #list which will contain cumulative new cases
    n=0 #container for weekly new cases
    with open('indiana_covid-19_data_fall_2022.txt') as fo: #context manager
        lines=fo.readlines() #split text into lines
        for string in lines:
            dates.append(string.split()[0]) #separate by whitespace, first group is start date
            n=n+float(string.split()[2]) #compute cumulative new cases
            y.append(n/1000) #append cumulative new cases to list (in thousands)
    
    for date in dates: #formatting dates on the graph
        year, m, d = date.split('-')
        dt = datetime.date(int(year), int(m), int(d))
        x.append(dt)

    ax.bar(x,y,width=7)
    ax.set_title('Weekly Positive COVID-19 Cases in Indiana') #plot title
    ax.set_xlabel('Date') #x label
    ax.set_ylabel('Number of Cases (in thousands)') #y label
    ax.set_ylim(0,2050)
    fig.autofmt_xdate() #format dates
    plt.show()
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
