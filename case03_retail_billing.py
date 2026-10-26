n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    if amount >= 2000:
        discount = amount * 0.10
    elif amount >= 1000:
        discount = amount * 0.05
    else:
        discount = 0

    final_amount = amount - discount
    total += final_amount

    print("\nProduct:", name)
    print("Amount:", round(amount, 2))
    print("Discount:", round(discount, 2))
    print("Final amount:", round(final_amount, 2))

print("\nTotal bill:", round(total, 2))