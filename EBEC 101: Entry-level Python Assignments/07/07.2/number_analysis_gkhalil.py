"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/31/2022

Description:
    This program calculates some data from a given list of numbers.

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

def get_number_list():
    l=[]
    for i in range(1,11): #i from 1 to 10 inclusive
        l.append(float(input(f"  number {i:2} of 10: "))) #gather numbers from user as floats and add to list
    return l

def main():
    print("Enter 10 numbers:")
    l=get_number_list()

    #get required metrics
    high=max(l)
    low=min(l)
    tot=sum(l)
    avg=sum(l)/len(l)
    
    #print gathered metrics
    print(f"Highest number: {high:.2f}")
    print(f"Lowest number: {low:.2f}")
    print(f"Total: {tot:.2f}")
    print(f"Average: {avg:.2f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
