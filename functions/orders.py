price_for_coffee = 1.50
price_for_water = 1.00
price_for_coke = 1.40
price_for_snacks = 2.00


def calculation(quantity, product):
    if product == "coffee":
        return f'{price_for_coffee * quantity:.2f}'
    elif product == "water":
        return f"{price_for_water * quantity:.2f}"
    elif product == "coke":
        return f"{price_for_coke * quantity:.2f}"
    elif product == "snacks":
        return f"{price_for_snacks * quantity:.2f}"


food = input()
number = int(input())
print(calculation(number, food))
