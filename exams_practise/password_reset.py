def take_odd(str):
    odd_elements = []
    for index in range(1, len(str), 2):
        odd_elements.append(str[index])
    return "".join(odd_elements)


def cut(my_string, my_index, my_length):
    new_string = my_string[:my_index] + my_string[my_index + my_length:]
    return new_string


def substitute_func(my_string, my_substring, my_substitute):
    if my_substring in my_string:
        my_string = my_string.replace(my_substring, my_substitute)
        return my_string
    else:
        return "Nothing to replace!"


string = input()
while True:
    command = input()
    if command == "Done":
        break

    split = command.split()
    action = split[0]
    if action == "TakeOdd":
        string = take_odd(string)
        print(string)
    elif action == "Cut":
        index = int(split[1])
        length = int(split[2])
        string = cut(string, index, length)
        print(string)
    elif action == "Substitute":
        substring = split[1]
        substitute = split[2]
        function = substitute_func(string, substring, substitute)
        if function == "Nothing to replace!":
            print(function)
        else:
            string = function
            print(string)
print(f"Your password is: {string}")
