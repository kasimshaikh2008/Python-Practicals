# Function Program 33

str1 = input("Enter a string: ")
result = list(map(lambda w: {w.upper(): [{v: w.lower().count(v)} for v in "aeiou" if v in w.lower()]}, str1.split()))
print(result)
