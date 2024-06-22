"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 08.5 - Number Reader
Date: 11/06/2022

Description:
    This program reads the contents of random_numbers.txt and determines some stats.

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
    with open('random_numbers.txt') as fo: #context manager
        lines=fo.readlines() #split text into lines
        l=len(lines) #number of numbers is equivalent to length of lines list
        integers=[] #to store list of integers
        for string in lines:
            integers.append(int(string)) #convert string to integer
        Min=min(integers)
        Max=max(integers)
        Sum=sum(integers)
        Avg=Sum/l
        
    print(f"{l:,} numbers were read from the file.")
    print(f"Min: {Min:,}")
    print(f"Max: {Max:,}")
    print(f"Sum: {Sum:,}")
    print(f"Avg: {Avg:,.1f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
