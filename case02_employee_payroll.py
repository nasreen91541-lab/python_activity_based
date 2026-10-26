name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentive = float(input("Enter incentive: "))

gross = basic + allowance + overtime + incentive

if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.15

net_salary = gross - deduction

print("\n--- Salary Statement ---")
print("Employee:", name)
print("Gross salary:", round(gross, 2))
print("Deduction:", round(deduction, 2))
print("Net salary:", round(net_salary, 2))