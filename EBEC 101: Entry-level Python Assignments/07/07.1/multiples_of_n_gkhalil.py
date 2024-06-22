"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/31/2022

Description:
    This program returns a list containing integers of a given list which are multiple of a number.

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

def multiples_of(a,b):
    multiples=[]
    for i in b: #going over all entries in list b
        if i % a == 0: #if list entry is a multiple of a
            multiples.append(i) #add it to the multiples list
    return multiples

def main():
    numbers=[19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]
    integer=13

    print("Original list of numbers:")
    print(f"  {numbers}")
    
    print(f"Numbers in the list that are multiples of {integer}:")
    print(f"  {multiples_of(13,numbers)}")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
