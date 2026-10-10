#Nelson Davis
#October 7th
#P3HW1 - Debugging


#Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: ')) 

#Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

#To do: determine lowest, highest, sum and average for grades

lowest_grade = min(grades)
highest_grade = max(grades)
total_grades = sum(grades)
average = total_grades / len(grades)

#Results
print('----------Results----------')
print(f"Lowest Grade: {lowest_grade:.2f}")
print(f"Highest Grade: {highest_grade:.2f}")
print(f"Sum of Grades: {total_grades:.2f}")
print(f"Average:       {average:.2f}")
print('----------------------------------------')

#Determine letter grade for average
if average >= 90:
    print('Your grade is: A') 
else:
    if average >=80:
        print('Your grade is: B')
    else:
        print('Your grade is: F') # To do: finish this

    


     
        


      