# Program 51: Menu-driven program to perform all list operations.

my_list = []
while True:
    print("\n1.Append 2.Insert 3.Extend 4.Remove 5.Pop 6.Sort 7.Reverse")
    print("8.Count 9.Index 10.Copy 11.Clear 12.Display 13.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = int(input("Enter element: "))
        my_list.append(x)
    elif ch == 2:
        pos = int(input("Enter position: "))
        x = int(input("Enter element: "))
        my_list.insert(pos, x)
    elif ch == 3:
        more = input("Enter elements to extend (space separated): ").split()
        for m in more:
            my_list.append(int(m))
    elif ch == 4:
        x = int(input("Enter element to remove: "))
        if x in my_list:
            my_list.remove(x)
        else:
            print("Element not found")
    elif ch == 5:
        if len(my_list) > 0:
            print("Popped element:", my_list.pop())
        else:
            print("List is empty")
    elif ch == 6:
        my_list.sort()
        print("List sorted")
    elif ch == 7:
        my_list.reverse()
        print("List reversed")
    elif ch == 8:
        x = int(input("Enter element to count: "))
        print("Count:", my_list.count(x))
    elif ch == 9:
        x = int(input("Enter element to find index: "))
        if x in my_list:
            print("Index:", my_list.index(x))
        else:
            print("Element not found")
    elif ch == 10:
        new_list = my_list.copy()
        print("Copied list:", new_list)
    elif ch == 11:
        my_list.clear()
        print("List cleared")
    elif ch == 12:
        print("List:", my_list)
    elif ch == 13:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
