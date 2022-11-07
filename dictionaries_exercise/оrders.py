def multiply(lst):
    # returns the quantity multiplied by the price
    return lst[0] * lst[1]


my_dict = {}
while True:
    command = input()
    if command == "buy":
        break

    product, price, quantity = command.split()
    if product not in my_dict:
        my_dict[product] = [float(price), int(quantity)]
    else:
        my_dict[product][0] = float(price)
        my_dict[product][1] += int(quantity)
print("\n".join([f"{product_name} -> {multiply(total_price):.2f}" for product_name, total_price in my_dict.items()]))
