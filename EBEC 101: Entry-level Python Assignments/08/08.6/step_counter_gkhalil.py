"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 08.6 - Step Counter
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
    with open('steps.txt') as fo: 
        lines=fo.readlines() 
        integers=[] 
        for string in lines:
            integers.append(int(string)) #convert string to integers
        
        steps=[]
        counter=0 #to keep track of index
        for i in range(12):
            if i in [0,2,4,6,7,9,11]: #months with 31 days
                steps.append(sum(integers[counter:counter+31])/31) #append average number of steps to list
                counter=counter+31 #update index
            elif i in [3,5,8,10]: #months with 30 days
                steps.append(sum(integers[counter:counter+30])/30)
                counter=counter+30
            elif i in [1]: #february with 28 days
                steps.append(sum(integers[counter:counter+28])/28)
                counter=counter+28

    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    
    print("The average steps taken each month were:")
    for i in range(12):
        print(f"{months[i]} : ".rjust(13),end='')
        print(f"{steps[i]:.2f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
