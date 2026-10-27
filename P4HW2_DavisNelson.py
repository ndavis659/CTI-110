#Nelson Davis
#October 24th
#P4HW2
#Salary calculator with loops

#Request employee info
name = input("Enter employee's name or 'done' to finish: ")

#Create accumulator variables for overtime pay, regular pay, gross pay and employee count
overtime_total = 0
regular_total = 0
gross_total = 0
employee_count = 0

while name != 'done':
    #Add employee count plus one
    employee_count += 1
    #Ask for employee info
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'S hourly pay rate? "))

    #Evaluate overtime
    if hours > 40:
        overtime_hours = hours - 40
        regular_pay = 40 * rate
        overtime_pay = overtime_hours * (rate * 1.5)
        gross_pay = regular_pay + overtime_pay


    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    #Add to accumulator totals
    overtime_total += overtime_pay
    regular_total += regular_pay
    gross_total += gross_pay

    #Display results for this employee
    print("--------------------------------")
    print("Employee name:", name)
    print(f'{"Hours worked": <15}{"Pay rate": <12}{"Overtime pay": <15}{"Regular pay": <15}{"Gross pay": <15}')
    print(f'{hours: <15}{rate: <12}{overtime_total: <15}{regular_pay: <15}{gross_pay: <15}')

    name = input("Enter emmployee's name or 'done' to finish: ")
print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime: $", format(overtime_total, ',.2f'))
print("Total amount paid for regular time: $", format(regular_total, ',.2f'))
print("Total amount paid in gross: $", format(gross_total, ',.2f'))






