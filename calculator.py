print("---------------- Calculator --------------")
ex = 1
while ex:
    f = False
    while not f:
        try:
            num = float(input("\n\nEnter a number: "))
            num2 = float(input("Enter a number 2 : "))
            f = True
            symbol = input("Symbol (1: + , 2: - ,3: /,4: *) : ")
        except ValueError:
            print("Not a valid number")

    match symbol:
        case "1":
            print(f"Result: {num + num2}")
        case "2":
            print(f"Result: {num - num2}")
        case "3":
            if num2 == 0:
                print("Error: Division by 0")
            else:
                print(f"Result: {num / num2}")
        case "4":
            print(f"Result: {num * num2}")
        case default:
            print("Invalid entry\n\n")

    ex = int(input("Press 0 to exit and any other number to continue\n"))

print("Exiting...\n")
