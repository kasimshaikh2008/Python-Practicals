# Program 60: Create a list of cities. Perform CRUD operations using a menu-driven approach.

cities = []
while True:
    print("\n1. Create  2. Read  3. Update  4. Delete  5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        city = input("Enter city name: ")
        cities.append(city)
        print("City added")
    elif choice == 2:
        if len(cities) == 0:
            print("List is empty")
        else:
            print("Cities:")
            for i in range(len(cities)):
                print(i + 1, cities[i])
    elif choice == 3:
        old = input("Enter city name to update: ")
        if old in cities:
            new = input("Enter new city name: ")
            cities[cities.index(old)] = new
            print("City updated")
        else:
            print("City not found")
    elif choice == 4:
        city = input("Enter city name to delete: ")
        if city in cities:
            cities.remove(city)
            print("City deleted")
        else:
            print("City not found")
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
