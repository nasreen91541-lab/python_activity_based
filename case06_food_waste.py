days = int(input("Enter number of days: "))

for i in range(days):
    print("\nDay", i + 1)

    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))

    if prepared < 0 or served < 0 or served > prepared:
        print("Invalid meal details")
    elif prepared == 0:
        print("No meals prepared")
    else:
        leftover = prepared - served
        waste_percentage = leftover / prepared * 100

        print("Leftover meals:", leftover)
        print("Wastage percentage:",
              round(waste_percentage, 2), "%")

        if waste_percentage > 20:
            print("Warning: High food wastage")
        else:
            print("Food wastage is acceptable")