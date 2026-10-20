# Program 47: Accept 15 numbers in a list. Separate into even and odd lists and display count, sum, maximum and minimum values.

numbers = []
for i in range(15):
    n = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(n)

even = []
odd = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("\nEven list:", even)
if len(even) > 0:
    print("Count:", len(even), "Sum:", sum(even), "Max:", max(even), "Min:", min(even))
else:
    print("No even numbers")

print("\nOdd list:", odd)
if len(odd) > 0:
    print("Count:", len(odd), "Sum:", sum(odd), "Max:", max(odd), "Min:", min(odd))
else:
    print("No odd numbers")
