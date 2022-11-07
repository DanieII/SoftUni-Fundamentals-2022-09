my_dict = {}
while True:
    command = input()
    if command == "statistics":
        break
    product, number = command.split(": ")
    if product not in my_dict:
        my_dict[product] = 0
    my_dict[product] += int(number)

print("Products in stock:")
for product, value in my_dict.items():
    print(f"- {product}: {value}")
print(f"""Total Products: {len(my_dict.keys())}
Total Quantity: {sum(my_dict.values())}"""
      )

# Another way
# my_dict = {}
# while True:
#     command = input()
#     if command == "statistics":
#         break
#     product, number = command.split(": ")
#     if product in my_dict:
#         my_dict[product] += int(number)
#         continue
#     my_dict[product] = int(number)
#
# print("Products in stock:")
# for product, value in my_dict.items():
#     print(f"- {product}: {value}")
# print(f"""Total Products: {len(my_dict.keys())}
# Total Quantity: {sum(my_dict.values())}"""
#       )
