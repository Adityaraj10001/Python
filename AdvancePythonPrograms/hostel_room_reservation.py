rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}

while True:
    print("\n--- Hostel Room Reservation System ---")
    print("1. View Available Rooms")
    print("2. Reserve a Room")
    print("3. Cancel Reservation")
    print("4. View All Reservations")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Rooms:")
        available = False
        for room in rooms:
            if rooms[room] is None:
                print("Room", room)
                available = True
        if not available:
            print("No rooms available.")

    elif choice == "2":
        room_number = int(input("Enter room number to reserve: "))
        if room_number in rooms:
            if rooms[room_number] is None:
                name = input("Enter your name: ")
                rooms[room_number] = name
                print("Room", room_number, "reserved for", name)
            else:
                print("Room already reserved.")
        else:
            print("Invalid room number.")

    elif choice == "3":
        room_number = int(input("Enter room number to cancel: "))
        if room_number in rooms and rooms[room_number] is not None:
            print("Reservation cancelled for", rooms[room_number])
            rooms[room_number] = None
        else:
            print("Invalid room number or not reserved.")

    elif choice == "4":
        print("\nRoom Reservations:")
        for room in rooms:
            if rooms[room] is None:
                print("Room", room, ": Available")
            else:
                print("Room", room, ": Reserved by", rooms[room])

    elif choice == "5":
        break

    else:
        print("Invalid choice.")