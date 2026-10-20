# Program 26: Sort employees by salary

employees = [("Aman", 45000), ("Riya", 60000), ("Karan", 52000)]
result = sorted(employees, key=lambda employee: employee[1])
print(result)
