"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 11/06/2022

Description:
    This program takes a string of English words and returns a string of equivalent words in Pig Latin.

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

def pig(s):
    s=s.lower() #to remove capital letters
    words=s.split() #split string into words
    piglow=[] #to store lowercase piglatin words

    for word in words:
        c=word[0] #store first character
        piglow.append(''.join([word[1:],c,'ay'])) #move first character to the end and add 'ay' 

    piglatin=' '.join(piglow)
    piglatin=piglatin.capitalize() #to capitalize first letter
    return piglatin


def main():
    eng=input("Enter a string: ")
    print(f"Pig latin: {pig(eng)}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
