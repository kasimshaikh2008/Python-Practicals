# Program 66: Accept a list of marks and assign grades (A, B, C, D, F) using list comprehension.

marks = []
data = input("Enter marks separated by space: ").split()
for x in data:
    marks.append(int(x))

grades = ["A" if m >= 90 else "B" if m >= 75 else "C" if m >= 60 else "D" if m >= 40 else "F" for m in marks]

print("Marks and Grades:")
for i in range(len(marks)):
    print(marks[i], "->", grades[i])
