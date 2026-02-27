#Event Tracker

entered = set()
rejected = set()

while True:
    print()
    print("1. Enter student  2.Reject student  3. Remove student  4. Show students  5. Quit ")
    choice = input("Choose: ").strip()
    
    if choice == "5":
        break
    elif choice == "4":
        print(f"Entered: {sorted(entered)}")
        print(f"Rejected: {sorted(rejected)}")
    elif choice == "1" or choice == "2":
        name = input("Name: ").strip()
        if choice == "1":
            if name in rejected:
                print("Already rejected!")
            else:
                entered.add(name)
                print("Added")
        else:
            if name in entered:
                print("Already entered!")
            else:
                rejected.add(name)
                print("Added")
    elif choice == "3":
        name = input("Name: ").strip()
        if name in entered:
            entered.remove(name)
            print("Removed")
        elif name in rejected:
            rejected.remove(name)
            print("Removed")
        else:
            print("Not found")
    else:
        print("Wrong choice!")