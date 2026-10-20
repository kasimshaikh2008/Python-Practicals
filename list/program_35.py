# Program 35: Filter out all vowels from a list of characters.

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'o', 'u', 'z']
result = [c for c in chars if c.lower() not in "aeiou"]
print("Original:", chars)
print("Without vowels:", result)
