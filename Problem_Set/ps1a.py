annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter portion of salary to save(Decimal form)(i.e. 0.1 for 10%): "))
total_cost = float(input("Enter the cost of dream home: "))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04

down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12

months = 0

while current_savings < down_payment:
    current_savings = current_savings + current_savings * (r / 12)
    
    current_savings = current_savings + monthly_salary * portion_saved
    
    months = months + 1

print("Number of months:", months)



OUTPUT

Enter annual salary: 120000
Enter portion of salary to save(Decimal form)(i.e. 0.1 for 10%): .10
Enter the cost of dream home: 1000000
Number of months: 183
