command = input()
total_price_without_tax = 0
customer_total_price = 0

while True:
    if command == "special" or command == "regular":
        break
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
    else:
        total_price_without_tax += current_price
    command = input()

taxes = total_price_without_tax * 0.2
total_price = total_price_without_tax + taxes
if total_price == 0:
    print("Invalid order!")
    exit()
elif command == "special":
    customer_total_price += 0.9 * (total_price)
elif command == "regular":
    customer_total_price += total_price

print(
    f"""Congratulations you've just bought a new computer!
Price without taxes: {total_price_without_tax:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {customer_total_price:.2f}$"""
)
