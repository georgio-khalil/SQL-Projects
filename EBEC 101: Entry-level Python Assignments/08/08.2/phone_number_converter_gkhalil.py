"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 11/06/2022

Description:
    This program takes a phone number string and returns its numeric equivalent.

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

def map(c): #separate function to handle mapping
    if c in ['A','B','C']:
        return '2'
    if c in ['D','E','F']:
        return '3'
    if c in ['G','H','I']:
        return '4'
    if c in ['J','K','L']:
        return '5'
    if c in ['M','N','O']:
        return '6'
    if c in ['P','Q','R','S']:
        return '7'
    if c in ['T','U','V']:
        return '8'
    if c in ['W','X','Y','Z']:
        return '9'

def convert_number(s):
    s=s.upper() #all uppercase to satisfy mapping function requirement
    number='' #container for phone number
    for c in s:
        if c.isalpha():
            c=map(c) #if character is alphabetical, map to numeric equivalent
        number=''.join([number,c]) #contruct numeric phone number
    return number

def main():
    n=input("Enter a telephone number: ")
    print(f"The phone number is {convert_number(n)}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
