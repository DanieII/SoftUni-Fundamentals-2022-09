import re

pattern = r"%([A-Z][a-z]+)%([^|$%.]+)*<(\w+)>([^|$%.]+)*\|(\d+)\|([^|$%.\d]+)*(\d+\.*\d*)\$"
total_income = 0
while True:
    command = input()
    if command == "end of shift":
        print(f"Total income: {total_income:.2f}")
        break

    result = re.search(pattern, command)
    if result:
        # Every group corresponds to the given element and even if the symbols in between match
        # they won't change the groups order
        name, product, quantity, price = result.group(1), result.group(3), result.group(5), result.group(7)
        final_price = int(quantity) * float(price)
        print(f"{name}: {product} - {final_price:.2f}")
        total_income += final_price
