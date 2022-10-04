lst_of_items = input().split("|")
budget = float(input())
lst_of_items_to_sell = []

for current_item_with_price in lst_of_items:
    current_item_price_after_raising = 0
    current_item = current_item_with_price.split("->")
    item_type = current_item[0]
    item_cost = float( current_item[1])
    if budget - item_cost < 0:
        continue
    elif item_type == "Clothes" and item_cost <= 50:
        budget -= item_cost
        current_item_price_after_raising = item_cost * 1.40
        lst_of_items_to_sell.append(current_item_price_after_raising)
    elif item_type == "Shoes" and item_cost <= 35:
        budget -= item_cost
        current_item_price_after_raising = item_cost * 1.40
        lst_of_items_to_sell.append(current_item_price_after_raising)
    elif item_type == "Accessories" and item_cost <= 20.50:
        budget -= item_cost
        current_item_price_after_raising = item_cost * 1.40
        lst_of_items_to_sell.append(current_item_price_after_raising)
print(*[f'{price:.2f}' for price in lst_of_items_to_sell])
print(f"Profit: {sum(lst_of_items_to_sell) - (sum(lst_of_items_to_sell) / 1.4):.2f}")
final_budget = sum(lst_of_items_to_sell) + budget
if final_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
