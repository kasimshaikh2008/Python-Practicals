# Program 65: Create a list using list comprehension for numbers from 1 to 100 and display squares, cubes, even, odd and multiples of 5.

numbers = [i for i in range(1, 101)]
squares = [n ** 2 for n in numbers]
cubes = [n ** 3 for n in numbers]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]
multiples_5 = [n for n in numbers if n % 5 == 0]

print("Squares:", squares)
print("\nCubes:", cubes)
print("\nEven numbers:", even)
print("\nOdd numbers:", odd)
print("\nMultiples of 5:", multiples_5)
