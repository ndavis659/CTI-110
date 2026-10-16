#Nelson Davis
#October 15th
#P4LAB2
#Use while loop and loop together

'''
Get integer from user
Determine if integer is positive or negative
if number is positive, display multiplicati on table
if number is negative, tell user program cannot accept it 
Ask user to run again?
If yes, run program
If no, end program
'''

run_again = 'yes'
while run_again != 'no':
    
    user_num = int(input("Enter an integer: "))



    if user_num >= 0:
    #Display multiplication for the value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values.")

    run_again = input("Would you run this program again?").lower()

#Loop has broken. User entered  'no'
print("Program is ending ....")
