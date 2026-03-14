item = str(input("What item would you like to buy?: "))
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You've bought {quantity}x {item}s")
print(f"Your total is ${total}.")