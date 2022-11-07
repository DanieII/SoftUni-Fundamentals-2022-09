products_and_prices = input().split()
products_to_search_for = input().split()
my_dict = {}
for index in range(0, len(products_and_prices), 2):
    food = products_and_prices[index]
    value = int(products_and_prices[index + 1])
    my_dict[food] = value
for item in products_to_search_for:
    if item in my_dict:
        quantity = my_dict[item]
        print(f"We have {quantity} of {item} left")
        continue
    print(f"Sorry, we don't have {item}")
