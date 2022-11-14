def check_length(name):
    if 3 <= len(name) <= 16:
        return True


def check_characters(name):
    for letter in name:
        if not (letter.isalnum() or letter == "-" or letter == "_"):
            return False
    return True


def redundant_symbols(name):
    for symbol in name:
        if symbol == " ":
            return False
    return True


def full_validation(name):
    if all([check_length(name), check_characters(name), redundant_symbols(name)]):
        return True


usernames = input().split(", ")
for username in usernames:
    if full_validation(username):
        print(username)
