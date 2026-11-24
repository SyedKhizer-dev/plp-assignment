from functools import reduce

employees = [
    {"name": "Khizer", "dept": "Engineering", "salary": 85000},
    {"name": "Rahul", "dept": "Engineering", "salary": 72000},
    {"name": "Priya", "dept": "HR", "salary": 55000},
    {"name": "Aman", "dept": "HR", "salary": 62000},
    {"name": "Sneha", "dept": "Marketing", "salary": 68000},
    {"name": "Arjun", "dept": "Marketing", "salary": 48000},
    {"name": "Zoya", "dept": "Engineering", "salary": 95000},
    {"name": "Karan", "dept": "HR", "salary": 75000},
    {"name": "Meera", "dept": "Marketing", "salary": 82000},
]

# (a)

engineering_employees = [
    employee["name"] for employee in employees if employee["dept"] == "Engineering"
]

print(engineering_employees)

# (b)
good_earning = {
    employee["name"]: employee["salary"]
    for employee in employees
    if employee["salary"] > 60000
}

print(good_earning)

# (c)
unique_dept = {employee["dept"] for employee in employees}
print(unique_dept)

# (d)

total_payroll = reduce(
    lambda amount, employee: amount + employee["salary"], employees, 0
)
print(total_payroll)

top_earners = sorted(employees, key=lambda item: item["salary"], reverse=True)[:3]
print(top_earners)
