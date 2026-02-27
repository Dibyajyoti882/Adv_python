#Room Allotment , Allot room, Vacate room, room info, exit

rooms = {"101": None, 
         "102": None,
         "103": None,
         "104": None,
         "105": None}

while True:
    ch = input("\n1.Allot  2.Vacate  3.Info  4.Exit : ")

    if ch == "1":
        room = input("Room no: ")
        if room in rooms and rooms[room] is None:
            rooms[room] = input("Student name: ")
            print("Allotted")
        else:
            print("Not Available")

    elif ch == "2":
        room = input("Room no: ")
        if room in rooms and rooms[room] is not None:
            rooms[room] = None
            print("Vacated")
        else:
            print("Empty")

    elif ch == "3":
        room = input("Room no: ")
        if room in rooms:
            print("Occupied by", rooms[room] if rooms[room] else "Vacant")
        else:
            print("Invalid Room")

    elif ch == "4":
        break

    else:
        print("Invalid Choice")

