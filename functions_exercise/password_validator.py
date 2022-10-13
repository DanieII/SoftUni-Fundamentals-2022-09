def password_length(my_pass):
    length = len(my_pass)
    if 6 <= length <= 10:
        return True
    return "Password must be between 6 and 10 characters"


def letters_and_digits(my_pass):
    if my_pass.isalnum():
        return True
    return "Password must consist only of letters and digits"


def two_digits(my_pass):
    digits = 0
    for current in my_pass:
        if current.isdigit():
            digits += 1
    if digits >= 2:
        return True
    return "Password must have at least 2 digits"


def validation(my_pass):
    first_validation = password_length(my_pass)
    second_validation = letters_and_digits(my_pass)
    third_validation = two_digits(my_pass)
    all_validations = [first_validation, second_validation, third_validation]
    # Check if all return True
    true_counter = 0
    for current in all_validations:
        if isinstance(current, bool):
            true_counter += 1
    if true_counter >= 3:
        return "Password is valid"
    # Adding all errors in a list in case not all validations were successful
    errors = []
    for current in all_validations:
        if isinstance(current, str):
            errors.append(current)
    # Returning errors separated with new lines
    return '\n'.join(map(str, errors))


password = input()
print(validation(password))
