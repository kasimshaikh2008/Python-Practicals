# Program 29: Display the top 3 students

students = [("Aman", 78), ("Riya", 92), ("Karan", 85), ("Ali", 95)]
top_three = sorted(students, key=lambda student: student[1], reverse=True)[:3]
print(top_three)
