# Program 12: Copy a list (shallow copy) and show it doesn't affect the original.

original = [1, 2, 3, 4]
copied = original.copy()
copied.append(99)
copied[0] = 100
print("Original list:", original)
print("Copied list:", copied)
