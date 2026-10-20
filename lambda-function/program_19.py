# Program 19: Find strings containing the letter a

words = ["apple", "sky", "banana", "grape"]
result = list(filter(lambda word: "a" in word, words))
print(result)
