# Program 37: Flatten a 2D list using a nested comprehension.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print("2D list:", matrix)
print("Flattened:", flat)
