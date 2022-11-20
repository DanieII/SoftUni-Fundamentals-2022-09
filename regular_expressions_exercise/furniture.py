import re

pattern = r">>([A-Za-z]+)<<(\d+[\d\.]*)!(\d+)"
furniture = []
total_price = 0
while True:
    command = input()
    if command == "Purchase":
        break

    current_result = re.findall(pattern, command)
    # if current_result: not used because if current_result is an empty list it can't be iterated through
    for element in current_result:
        current_furniture = element[0]
        current_price = float(element[1])
        current_quantity = int(element[2])
        furniture.append(current_furniture)
        total_price += current_price * current_quantity
print(f"Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_price:.2f}")
