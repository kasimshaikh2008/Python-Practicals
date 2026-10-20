# Program 43: Create a list of 10 student marks. Perform insertion, deletion, updating, sorting, reversing, and display highest, lowest and average marks.

marks = [56, 78, 90, 45, 67, 88, 72, 34, 95, 61]
print("Marks:", marks)

marks.append(80)
print("After insertion:", marks)

marks.remove(34)
print("After deletion:", marks)

marks[0] = 60
print("After updating first mark:", marks)

marks.sort()
print("Sorted:", marks)

marks.reverse()
print("Reversed:", marks)

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Average marks:", sum(marks) / len(marks))
