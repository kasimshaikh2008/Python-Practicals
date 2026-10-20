# Program 49: Accept a sentence, convert it into a list of words, count occurrence of each word and remove repeated words.

sentence = input("Enter a sentence: ")
words = sentence.lower().split()
print("List of words:", words)

count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
print("Word count:", count)

unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)
print("After removing repeated words:", unique_words)
