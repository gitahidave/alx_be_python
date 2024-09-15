#User's financial details
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

#Calculating user's monthly savings
monthly_savings = monthly_income - monthly_expenses

#Project annual savings
annual_savings = monthly_savings * 12
project_savings = annual_savings + annual_savings * 0.05
#Assuming the simple annual interest rate of 5%

print("Your monthly savings are:", monthly_savings)
print("Your projected savings after one year, with interest, is", project_savings)
 