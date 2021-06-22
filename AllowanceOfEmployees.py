# AllowanceOfEmployees.py
Allowance_Array = []
Allowance = 0
NetSalary = 0
for i in range(10):
    Salary = int(input('Enter the basic salary of the employee: '))
    Allowance_Array.append(Salary)
for i in range(10):
    if 3000 > Allowance_Array[i] >= 2000:
        Allowance = Allowance_Array[i] * 0.15
        NetSalary = Allowance + Allowance_Array[i]
    elif 4500 > Allowance_Array[i] >= 3000:
        Allowance = Allowance_Array[i] * 0.10
        NetSalary = Allowance + Allowance_Array[i]
    elif 6000 > Allowance_Array[i] >= 4500:
        Allowance = Allowance_Array[i] * 0.08
        NetSalary = Allowance + Allowance_Array[i]
    elif Allowance_Array[i] >= 6000:
        Allowance = Allowance_Array[i] * 0.06
        NetSalary = Allowance + Allowance_Array[i]
    else:
        Allowance = Allowance_Array[i] * 0.20
        NetSalary = Allowance + Allowance_Array[i]
print(f'The Net Salary is {NetSalary}')