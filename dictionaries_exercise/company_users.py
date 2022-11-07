def check_for_the_same_id(dictionary, name, user):
    if user in dictionary[name]:
        return True


my_dict = {}
while True:
    command = input()
    if command == "End":
        break

    company, current_id = command.split(" -> ")
    if company not in my_dict:
        my_dict[company] = [current_id]
    else:
        if not check_for_the_same_id(my_dict, company, current_id):
            my_dict[company].append(current_id)
for key, value in my_dict.items():
    print(key)
    print("\n".join([f"-- {x}" for x in value]))
