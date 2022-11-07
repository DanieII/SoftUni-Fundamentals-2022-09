my_dict = {"shards": 0, "fragments": 0, "motes": 0}
flag = False
while True:
    sequence_of_numbers_and_materials = input().split()
    for element in range(0, len(sequence_of_numbers_and_materials), 2):
        number = int(sequence_of_numbers_and_materials[element])
        material = sequence_of_numbers_and_materials[element + 1].lower()
        if material not in my_dict:
            my_dict[material] = 0
        my_dict[material] += number
        if my_dict[material] >= 250:
            my_dict[material] -= 250
            if material == "shards":
                legendary_item = "Shadowmourne"
            elif material == "fragments":
                legendary_item = "Valanyr"
            elif material == "motes":
                legendary_item = "Dragonwrath"
            print(f"{legendary_item} obtained!")
            flag = True
            break
    if flag:
        break
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Judge 100/100
# my_dict = {"shards": 0, "fragments": 0, "motes": 0}
# obtained = False
# while not obtained:
#     sequence_of_numbers_and_materials = input().split()
#     for element in range(0, len(sequence_of_numbers_and_materials), 2):
#         number = int(sequence_of_numbers_and_materials[element])
#         material = sequence_of_numbers_and_materials[element + 1].lower()
#         if material not in my_dict:
#             my_dict[material] = 0
#         my_dict[material] += number
#         if my_dict["shards"] >= 250:
#             my_dict["shards"] -= 250
#             print(f"Shadowmourne obtained!")
#             obtained = True
#         elif my_dict["fragments"] >= 250:
#             my_dict["fragments"] -= 250
#             print(f"Valanyr obtained!")
#             obtained = True
#         elif my_dict["motes"] >= 250:
#             my_dict["motes"] -= 250
#             print(f"Dragonwrath obtained!")
#             obtained = True
#         if obtained:
#             break
#     if obtained:
#         break
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
