# Program 41: Create a multiplication table (list of lists) using comprehension.

table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
for row in table:
    print(row)
