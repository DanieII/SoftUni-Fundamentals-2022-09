everything = input().split()
my_dict = {}

for index in range(0, len(everything), 2):
    food = everything[index]
    value = int(everything[index + 1])
    my_dict[food] = value
print(my_dict)


# Another solution
# food = []
# values = []
# for element in everything:
#     if everything.index(element) % 2 == 0 or everything.index(element) == 0:
#         food.append(element)
#     else:
#         values.append(int(element))
#
# for index in range(len(food)):
#     current_food = food[index]
#     current_value = values[index]
#     my_dict[current_food] = current_value
# print(my_dict)
