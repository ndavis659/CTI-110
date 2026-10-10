#Nelson Davis
#October 8th
#Salary calculator
#P3HW2

#Request employee info
name = input("Enter employee name:")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly rate: "))

#Evaluate overtime
if hours > 40:
    #Calculate overtime
    overtime_hours = hours - 40
    #Calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    #Calculate salary for regular hours
    regular_pay = 40 * rate
    #Calculate Gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

#Display results
print("----------------------------------------------------")
print("Employee Name:", name)
print(f'{"Hours worked": <15}{"Pay rate": <12}{"Overtime pay": <15}{"Regular hours": <15}{"Overtime pay"}:<12{"Gross pay": <12}')
print("-----------------------------------")
print(f'{hours: <15}{rate: <12}{overtime_pay: <12}{regular_pay: <15}{gross_pay: <12}')
