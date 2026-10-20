# Program 40: Extract words longer than 5 letters from a sentence.

sentence = "Python is a very powerful programming language for beginners"
words = sentence.split()
long_words = [w for w in words if len(w) > 5]
print("Words longer than 5 letters:", long_words)
