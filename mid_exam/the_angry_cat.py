def cheap(prices, index, cost):
    uncalculated_left = prices[:index]
    uncalculated_right = prices[index + 1:]
    left_side = []
    for i in uncalculated_left:
        if i < cost:
            left_side.append(i)
    right_side = []
    for j in uncalculated_right:
        if j < cost:
            right_side.append(j)

    damage_to_left = sum(left_side)
    damage_to_right = sum(right_side)
    if damage_to_left == damage_to_right:
        position = "Left"
        return f"{position} - {damage_to_left}"
    elif damage_to_left > damage_to_right:
        position = "Left"
        return f"{position} - {damage_to_left}"
    elif damage_to_right > damage_to_left:
        position = "Right"
        return f"{position} - {damage_to_right}"


def expensive(prices, index, cost):
    uncalculated_left = prices[:index]
    uncalculated_right = prices[index + 1:]
    left_side = []
    for i in uncalculated_left:
        if i >= cost:
            left_side.append(i)
    right_side = []
    for j in uncalculated_right:
        if j >= cost:
            right_side.append(j)

    damage_to_left = sum(left_side)
    damage_to_right = sum(right_side)
    if damage_to_left == damage_to_right:
        position = "Left"
        return f"{position} - {damage_to_left}"
    elif damage_to_left > damage_to_right:
        position = "Left"
        return f"{position} - {damage_to_left}"
    elif damage_to_right > damage_to_left:
        position = "Right"
        return f"{position} - {damage_to_right}"


all_prices = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()
value = all_prices[entry_point]

if type_of_items == "cheap":
    print(cheap(all_prices, entry_point, value))
elif type_of_items == "expensive":
    print(expensive(all_prices, entry_point, value))
