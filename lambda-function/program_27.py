# Program 27: Sort student records by marks

students = [
    {"name": "Aman", "marks": 78},
    {"name": "Riya", "marks": 92},
    {"name": "Karan", "marks": 85}
]
result = sorted(students, key=lambda student: student["marks"])
print(result)
