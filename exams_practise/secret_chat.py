def insert_space_func(text, indx):
    new_string = text
    if 0 <= indx <= len(text):
        new_string = text[:indx] + " " + text[indx:]
    return new_string


def reverse_func(text, sub):
    if sub not in text:
        return False
    else:
        # Only the first occurrence has to be cut/deleted
        new_string = text.replace(sub, "", 1)
        new_string = new_string + sub[::-1]
        return new_string


def change_all_func(text, sub, replace):
    new_string = text
    if sub in text:
        new_string = text.replace(sub, replace)
    return new_string


string = input()
while True:
    command = input()
    if command == "Reveal":
        break

    split = command.split(":|:")
    action = split[0]
    if action == "InsertSpace":
        index = int(split[1])
        string = insert_space_func(string, index)
        print(string)
    elif action == "Reverse":
        substring = split[1]
        if not reverse_func(string, substring):
            print("error")
        else:
            string = reverse_func(string, substring)
            print(string)
    elif action == "ChangeAll":
        substring = split[1]
        replacement = split[2]
        string = change_all_func(string, substring, replacement)
        print(string)
print(f"You have a new text message: {string}")
