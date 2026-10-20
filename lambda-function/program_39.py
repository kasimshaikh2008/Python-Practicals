# Program 39: Find IT employees earning above 50,000

employees = [
    {"name": "Aman", "department": "IT", "salary": 60000},
    {"name": "Riya", "department": "HR", "salary": 70000},
    {"name": "Karan", "department": "IT", "salary": 45000},
    {"name": "Ali", "department": "IT", "salary": 80000}
]
result = list(filter(lambda emp: emp["department"] == "IT" and emp["salary"] > 50000, employees))
print(result)
