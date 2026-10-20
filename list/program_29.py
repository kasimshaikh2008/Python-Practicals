# Program 29: Remove None or empty values from a list.

data = [1, None, "hello", "", 5, None, "world", ""]
clean = []
for item in data:
    if item != None and item != "":
        clean.append(item)
print("Original:", data)
print("Cleaned:", clean)
