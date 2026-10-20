# Program 28: Find employees earning above 50,000

employees = [
    {"name": "Aman", "salary": 45000},
    {"name": "Riya", "salary": 60000},
    {"name": "Karan", "salary": 75000}
]
result = list(filter(lambda employee: employee["salary"] > 50000, employees))
print(result)
