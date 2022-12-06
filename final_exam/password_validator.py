def make_upper_func(index, string):
    new_letter = string[index].upper()
    string = string[:index] + new_letter + string[index + 1:]
    return string


def make_lower_func(index, string):
    new_letter = string[index].lower()
    string = string[:index] + new_letter + string[index + 1:]
    return string


def insert_func(indx, chr, string):
    new_string = string
    if not 0 <= indx < len(string):
        return new_string
    new_string = string[:indx] + chr + string[indx:]
    return new_string


def replace_func(character, val, string):
    new_value = chr(ord(character) + val)
    string = string.replace(character, new_value)
    return string


password = input()
while True:
    command = input()
    if command == "Complete":
        break

    split = command.split()
    action = split[0]
    if action == "Make":
        indx = int(split[2])
        if split[1] == "Upper":
            password = make_upper_func(indx, password)
            print(password)
        elif split[1] == "Lower":
            password = make_lower_func(indx, password)
            print(password)
    elif action == "Insert":
        index = int(split[1])
        char = split[2]
        password = insert_func(index, char, password)
        print(password)
    elif action == "Replace":
        char = split[1]
        value = int(split[2])
        password = replace_func(char, value, password)
        print(password)
    elif action == "Validation":
        if not len(password) >= 8:
            print("Password must be at least 8 characters long!")

        for symbol in password:
            if not symbol.isalnum() and symbol != "_":
                print("Password must consist only of letters, digits and _!")
                break

        uppercase_count = 0
        for symbol in password:
            if symbol.isupper():
                uppercase_count += 1
        if uppercase_count == 0:
            print("Password must consist at least one uppercase letter!")

        lowercase_count = 0
        for symbol in password:
            if symbol.islower():
                lowercase_count += 1
        if lowercase_count == 0:
            print("Password must consist at least one lowercase letter!")

        digit_count = 0
        for symbol in password:
            if symbol.isdigit():
                digit_count += 1
        if digit_count == 0:
            print("Password must consist at least one digit!")
