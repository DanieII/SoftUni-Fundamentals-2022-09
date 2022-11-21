def move_func(my_string, number):
    string_to_move = my_string[:number]
    new_string = my_string[number:] + string_to_move
    return new_string


def insert_func(my_string, my_index, my_value):
    new_string = my_string[:my_index] + my_value + my_string[my_index:]
    return new_string


def change_all_func(my_string, old, new):
    new_string = my_string.replace(old, new)
    return new_string


string = input()
while True:
    command = input()
    if command == "Decode":
        break

    split = command.split("|")
    action = split[0]

    if action == "Move":
        number_of_letters = int(split[1])
        string = move_func(string, number_of_letters)
    elif action == "Insert":
        index = int(split[1])
        value = split[2]
        string = insert_func(string, index, value)
    elif action == "ChangeAll":
        substring = split[1]
        replacement = split[2]
        string = change_all_func(string, substring, replacement)
print(f"The decrypted message is: {string}")
