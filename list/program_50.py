# Program 50: Create a nested list containing student details (Roll No., Name, Marks). Display topper details and sort students according to marks.

students = [
    [101, "Amit", 78],
    [102, "Neha", 92],
    [103, "Rahul", 65],
    [104, "Priya", 85]
]

topper = students[0]
for s in students:
    if s[2] > topper[2]:
        topper = s
print("Topper details:")
print("Roll No:", topper[0], "Name:", topper[1], "Marks:", topper[2])

n = len(students)
for i in range(n):
    for j in range(0, n - i - 1):
        if students[j][2] < students[j + 1][2]:
            students[j], students[j + 1] = students[j + 1], students[j]

print("\nStudents sorted by marks (highest first):")
for s in students:
    print(s[0], s[1], s[2])
