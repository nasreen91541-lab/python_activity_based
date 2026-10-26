units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
else:
    bill = 0

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    fixed_charge = 50
    total = bill + fixed_charge

    print("Energy charge:", bill)
    print("Fixed charge:", fixed_charge)
    print("Total electricity bill:", total)