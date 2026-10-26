attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
required = float(input("Enter required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details")
elif required <= 0 or required > 100:
    print("Invalid required percentage")
else:
    percentage = attended / conducted * 100

    print("Current attendance:", round(percentage, 2), "%")

    if percentage >= required:
        print("Attendance requirement satisfied")
    else:
        needed = 0

        while ((attended + needed) /
               (conducted + needed) * 100) < required:
            needed += 1

        print("Additional classes required:", needed)
        print("Attendance after recovery:",
              round((attended + needed) /
                    (conducted + needed) * 100, 2), "%")