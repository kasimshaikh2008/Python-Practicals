# Program 22: Find numbers greater than the average

numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
result = list(filter(lambda n: n > average, numbers))
print("Average:", average)
print("Above average:", result)
