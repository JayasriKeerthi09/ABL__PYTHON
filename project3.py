name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
month = input("Enter month (e.g., October 2026): ")
basic_pay = float(input("Enter basic pay: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives/bonus: "))
hra = 0.20 * basic_pay
da = 0.10 * basic_pay
travel_allowance = 2000
total_allowances = hra + da + travel_allowance
overtime_pay = overtime_hours * overtime_rate
gross_salary = basic_pay + total_allowances + overtime_pay + incentives
def calculate_tax(income):
    tax = 0
    if income > 70000:
        tax += (income - 70000) * 0.20
        income = 70000
    if income > 40000:
        tax += (income - 40000) * 0.10
        income = 40000
    if income > 20000:
        tax += (income - 20000) * 0.05
    return tax
income_tax = calculate_tax(gross_salary)
pf = 0.12 * basic_pay
professional_tax = 200 if gross_salary > 15000 else 0
insurance = 500
total_deductions = income_tax + pf + professional_tax + insurance
net_salary = gross_salary - total_deductions
print("\n" + "=" * 50)
print("                SALARY STATEMENT")
print("=" * 50)
print(f"Employee Name : {name}")
print(f"Employee ID   : {emp_id}")
print(f"Month         : {month}")
print("-" * 50)
print("EARNINGS")
print(f"{'Basic Pay':<30}{basic_pay:>15,.2f}")
print(f"{'HRA (20%)':<30}{hra:>15,.2f}")
print(f"{'DA (10%)':<30}{da:>15,.2f}")
print(f"{'Travel Allowance':<30}{travel_allowance:>15,.2f}")
print(f"{'Overtime Pay':<30}{overtime_pay:>15,.2f}")
print(f"{'Incentives':<30}{incentives:>15,.2f}")
print("-" * 50)
print(f"{'GROSS SALARY':<30}{gross_salary:>15,.2f}")
print("-" * 50)
print("DEDUCTIONS")
print(f"{'Income Tax (Progressive)':<30}{income_tax:>15,.2f}")
print(f"{'Provident Fund (12%)':<30}{pf:>15,.2f}")
print(f"{'Professional Tax':<30}{professional_tax:>15,.2f}")
print(f"{'Health Insurance':<30}{insurance:>15,.2f}")
print("-" * 50)
print(f"{'TOTAL DEDUCTIONS':<30}{total_deductions:>15,.2f}")
print("=" * 50)
print(f"{'NET SALARY (Take Home)':<30}{net_salary:>15,.2f}")
print("=" * 50)
print("   Deductions as % of Gross: {:.2f}%".format(
    (total_deductions / gross_salary) * 100))
print("=" * 50)