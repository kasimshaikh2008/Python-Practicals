# Program 20: Remove empty strings

words = ["Python", "", "Lambda", "", "AI"]
result = list(filter(lambda word: word != "", words))
print(result)
