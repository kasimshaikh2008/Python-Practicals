# Program 55: Create a list of strings. Display longest, shortest, strings starting with a vowel and strings ending with a consonant.

words = ["apple", "banana", "orange", "kiwi", "umbrella", "mango", "egg"]

longest = words[0]
shortest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
    if len(w) < len(shortest):
        shortest = w
print("Longest string:", longest)
print("Shortest string:", shortest)

vowels = "aeiouAEIOU"
start_vowel = []
end_consonant = []
for w in words:
    if w[0] in vowels:
        start_vowel.append(w)
    if w[-1] not in vowels:
        end_consonant.append(w)
print("Strings starting with a vowel:", start_vowel)
print("Strings ending with a consonant:", end_consonant)
