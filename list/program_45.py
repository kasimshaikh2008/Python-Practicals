# Program 45: Create a shopping list. Menu-driven program to add, remove, search, update, sort and display items.

items = []
while True:
    print("\n1. Add  2. Remove  3. Search  4. Update  5. Sort  6. Display  7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter item to add: ")
        items.append(item)
        print("Item added")
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in items:
            items.remove(item)
            print("Item removed")
        else:
            print("Item not found")
    elif choice == 3:
        item = input("Enter item to search: ")
        if item in items:
            print("Item found at position", items.index(item) + 1)
        else:
            print("Item not found")
    elif choice == 4:
        old = input("Enter item to update: ")
        if old in items:
            new = input("Enter new item: ")
            items[items.index(old)] = new
            print("Item updated")
        else:
            print("Item not found")
    elif choice == 5:
        items.sort()
        print("List sorted")
    elif choice == 6:
        print("Shopping list:", items)
    elif choice == 7:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
