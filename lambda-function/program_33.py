# Program 33: Find squares of even numbers

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda n: n % 2 == 0, numbers)
result = list(map(lambda n: n ** 2, even_numbers))
print(result)
