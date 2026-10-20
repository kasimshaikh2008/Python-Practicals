# Program 42: Filter numbers divisible by both 3 and 5.

result = [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]
print("Numbers divisible by both 3 and 5:", result)
