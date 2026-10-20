# Program 37: Select words starting with a vowel

words = ["orange", "apple", "banana", "umbrella", "kiwi", "egg"]
selected = filter(lambda word: word[0].lower() in "aeiou", words)
result = sorted(selected, key=lambda word: len(word))
print(result)
