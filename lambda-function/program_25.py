# Program 25: Sort students by marks

students = [("Aman", 78), ("Riya", 92), ("Karan", 85)]
result = sorted(students, key=lambda student: student[1])
print(result)
