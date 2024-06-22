"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 09/22/2022

Description:
    This program displays the letter grades corresponding to 5 given scores. The program then displays the average of all scores and the corresponding letter grade.

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

def get_valid_score():
    while 1:
        n=float(input("Enter a score: "))
        if n>=0 and n<=100: #if valid number, return and exit function
            return n
        print("  Invalid Input. Please try again.")

def calc_average(list):
    return sum(list)/len(list) #computing average of a list of numbers

def determine_grade(n): #assume that n is valid and start from F condition
    if n<64:
        return 'F'
    elif n<73:
        return 'D'
    elif n<82:
        return 'C'
    elif n<92:
        return 'B'
    return 'A' #by elimination, grade is A

def main():
    scores=[]
    for i in range (5): #get 5 scores
        n=get_valid_score()
        print(f"  The letter grade for {n:.1f} is {determine_grade(n)}.")
        scores.append(n)

    avg=calc_average(scores)
    print("\nResults:")
    print(f"  The average score is {avg:.2f}.")
    print(f"  The letter grade for {avg:.2f} is {determine_grade(avg)}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
