annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter portion of salary to save(Decimal form)(i.e. 0.1 for 10%): "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise (as decimal): "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04 
monthly_salary = annual_salary / 12

down_payment = total_cost * portion_down_payment

months = 0

while current_savings < down_payment:
    months = months + 1

    current_savings = current_savings + current_savings * (r / 12)
    current_savings = current_savings + monthly_salary * portion_saved

    if months % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12

print("Number of months:", months)


OUTPUT

Enter your starting annual salary: 120000
Enter portion of salary to save(Decimal form)(i.e. 0.1 for 10%): .05
Enter the cost of your dream home: 500000
Enter the semi-annual raise (as decimal): .03
Number of months: 142
