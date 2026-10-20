# Function Program 22

words = ["madam", "hello", "level", "python", "nitin", "radar"]
result = list(filter(lambda w: w == w[::-1], words))
print("Palindrome words:", result)
