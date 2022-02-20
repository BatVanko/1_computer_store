command = input()
price_without_taxes = 0
special = False


while True:
    if command == "special":
        special = True
        break
    if command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")

    else:
        price_without_taxes += price

    command = input()

taxes = price_without_taxes * 0.2
total_price = price_without_taxes + taxes
if special:
    total_price *= 0.9
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")


