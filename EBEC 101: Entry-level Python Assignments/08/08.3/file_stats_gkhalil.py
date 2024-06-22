"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 08.3 - File Stats
Date: 11/06/2022

Description:
    This program reads the contents of a file and determines the number of words, lines, and words per line.

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
    with open('frontiero_v_richardson.txt') as fo: #context manager
        lines=fo.readlines() #split text into lines
        l=len(lines) #number of lines is equivalent to length of lines list
        w=0 #container for number of words
        for sentence in lines:
            w_line=len(sentence.split()) #number of words per line, split by whitespace
            w=w+w_line #compute total number of words
    print(f"Total number of words: {w}")
    print(f"Total number of lines: {l}")
    print(f"Average number of words per line: {w/l:.1f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
