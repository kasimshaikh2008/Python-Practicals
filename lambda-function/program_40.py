# Program 40: Rank students from highest to lowest marks

students = [("Aman", 78), ("Riya", 92), ("Karan", 85), ("Ali", 95)]
ranking = sorted(students, key=lambda student: student[1], reverse=True)
for rank, (name, marks) in enumerate(ranking, start=1):
    print(f"Rank {rank}: {name} - {marks} marks")
