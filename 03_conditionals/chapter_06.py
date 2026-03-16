seat_type = input("Choose seat type (sleeper,ac,luxury,general) : ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper selection")
    case "ac":
        print("Selecting AC")
    case "general":
        print("Selecting General")
    case "luxury":
        print("Luxury")
    case _:
        print("Invalid Seat Type")