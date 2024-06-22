"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 09/22/2022

Description:
    This program calculates the sum of numbers not divisible by 3 that fall between 2 given numbers.

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

def lucky_sum(a,b):
    sum = 0
    if a>b: #if first argument larger than second, switch arguments using a temporary variable
        temp=a
        a=b
        b=temp
    for i in range (a,b+1):
        if i%3 != 0: #if number not divisible by 3
            sum = sum+i
    return sum
    

def main():
    a=int(input("Enter the first integer: "))
    b=int(input("Enter the second integer: "))

    print(f"The sum of the lucky numbers is {lucky_sum(a,b):,}.")
        
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
