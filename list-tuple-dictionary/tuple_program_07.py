# Tuple Program 7
n = int(input("How many cities: "))
cities = ()
for i in range(n):
    c = input("Enter city name: ")
    cities = cities + (c,)
print(cities)
