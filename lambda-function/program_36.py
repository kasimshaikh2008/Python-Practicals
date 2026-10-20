# Program 36: Select passed students and sort by marks

students = [("Aman", 35), ("Riya", 82), ("Karan", 48), ("Ali", 29)]
passed = filter(lambda student: student[1] >= 35, students)
result = sorted(passed, key=lambda student: student[1])
print(result)
