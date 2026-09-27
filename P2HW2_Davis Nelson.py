#Nelson Davis
#September 26th
#P2HW2
#Calculates the lowest grade, and average those grades out 

#Pseudocode to write a program that ask to enter test grades using a separate input statement:

#Step 2 and 3: Prompt for Grades and Store grades in a list

grade1 = float(input("Enter grade for Module 1:"))


grade2 = float(input("Enter grade for Module 2:"))


grade3 = float(input("Enter grade for Module 3:"))


grade4 = float(input("Enter grade for Module 4:"))

grade5 = float(input("Enter grade for Module 5:"))


grade6 = float(input("Enter grade for Module 6:"))

grades = [grade1, grade2, grade3, grade4, grade5, grade6]
#Calculate required results

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

#Format output two Decimal places
print("\n--- Grade Results ---")
print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade:}")
print(f"sum of Grades: {sum_of_grades}")
print(f"Average:       {average_grade:.2f}")
print("-------------------------------")




