item = input("What Do you want to buy?: ")
price = float(input("Enter the price?: $"))
quantity = int(input("How many would you buy?: "))

total = price * quantity

print(f"You want to buy {quantity} x {item}.")
print(f"The price would be ${total}")