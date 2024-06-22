"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/14/2022

Description:
    This program lets the user play a game of Rock, Paper, Scissors against the computer using random choices.

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

def get_computer_choice():
    c_choice = r.randrange(1,4) #randomly return 1, 2, or 3
    if c_choice == 1:
        return 'rock'
    elif c_choice == 2:
        return 'paper'
    elif c_choice == 3:
        return 'scissors'

def get_player_choice():
    while 1:
        p_choice=(input("Choose rock, paper, or scissors: "))
        if p_choice in ['rock','paper','scissors']: #check for valid input
            return p_choice
        print("You made an invalid choice. Please try again.")

def get_winner(c,p):
    if c==p:
        return 'tie'
    if any([c == 'rock' and p == 'scissors',c == 'paper' and p == 'rock', c =='scissors' and p =='paper']): #computer winning cases
        return 'computer'
    return 'player' #when it's not a tie or computer win, it's a player win

def main():
    while 1:
        c_choice = get_computer_choice()
        p_choice = get_player_choice()
        print(f"  The computer chose {c_choice}, and you chose {p_choice}.")
        if get_winner(c_choice,p_choice) == 'tie':
            print("  It's a tie. Starting over.\n")
            continue #repeat the loop
        if get_winner(c_choice,p_choice) == 'computer':
            print(f"  {c_choice} beats {p_choice}")
            print("  You lost.  Better luck next time.")
            print("Thanks for playing.")
            break
        if get_winner(c_choice,p_choice) == 'player':
            print(f"  {p_choice} beats {c_choice}")
            print("  You won the game!")
            print("Thanks for playing.")
            break

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
