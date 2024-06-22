"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/17/2022

Description:
    This program predicts the approximate size of a population of organisms.

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
    #gather inputs
    p = float(input("Starting population, in thousands: "))
    inc= float(input("Average daily increase, in percent: "))
    days = int(input("Number of days to multiply: "))

    print("Day   Approx. Pop")
    for i in range (days+1):
        print(f"{i:3}{p:14,.3f}") #specifying width of string to align table
        p=p*(1+inc/100) #population increase starts after first day


        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
