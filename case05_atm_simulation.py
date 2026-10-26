balance = float(input("Enter opening balance: "))
deposits = 0
withdrawals = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif choice == 1:
        balance += amount
        deposits += amount
        print("Deposit successful")
    elif choice == 2:
        if amount <= balance and amount <= 10000:
            balance -= amount
            withdrawals += amount
            print("Withdrawal successful")
        else:
            print("Withdrawal rejected")
    else:
        print("Invalid choice")

print("\n--- Transaction Summary ---")
print("Total deposits:", deposits)
print("Total withdrawals:", withdrawals)
print("Final balance:", round(balance, 2))