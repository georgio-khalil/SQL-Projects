"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/31/2022

Description:
    This program displays statistics from a simulation of 1,000,000 rolls of a pair of dice.

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
import random as r

"""Write new functions below this line (starting with unit 4)."""

def roll_d6(): 
    return r.randint(1,6) #one roll of one six-sided die

def get_2d6_rolls(n):
    l=[]
    for i in range(n): 
        sum=roll_d6()+roll_d6() #total of rolling 2d6
        l.append(sum) #gather totals in list
    return l

def main():
    l=get_2d6_rolls(1000000) #1 million rolls of 2d6

    print("Roll  Frequency")
    for i in range (2,13):
        print(f"{i:3}   {l.count(i)/len(l):7.2%}") #formatting to match desired output format

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
