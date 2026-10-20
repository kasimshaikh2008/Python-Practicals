# Program 17: Find words with more than 5 characters

words = ["apple", "banana", "grapes", "kiwi", "orange"]
result = list(filter(lambda word: len(word) > 5, words))
print(result)
