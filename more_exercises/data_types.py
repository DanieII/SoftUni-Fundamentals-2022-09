def action(my_string, my_number):
    try:
        transformed_number = int(my_number)
    except ValueError:
        transformed_number = my_number
    if my_string == "int":
        return transformed_number * 2
    if my_string == "real":
        return f"{transformed_number * 1.5:.2f}"
    if my_string == "string":
        return f"${transformed_number}$"


string = input()
number = input()
print(action(string, number))


# def action(my_string, my_number):
#     if my_string == "int":
#         return int(my_number) * 2
#     if my_string == "real":
#         return f"{int(my_number) * 1.5:.2f}"
#     if my_string == "string":
#         return f"${my_number}$"
#
#
# string = input()
# number = input()
# print(action(string, number))


# def action(my_string):
#     number = input()
#     if my_string == "int":
#         return int(number) * 2
#     if my_string == "real":
#         return f"{int(number) * 1.5:.2f}"
#     if my_string == "string":
#         return f"${number}$"
#
#
# string = input()
# print(action(string))
