# str1 = input()
# str2 = input()
# string_1 = list(str1)
# string_2 = list(str2)
# len_of_strings = len(str1)
# for current_digit in range(len_of_strings):
#     if string_1[current_digit] == " ":
#         continue
#     elif string_1[current_digit] != string_2[current_digit]:
#         string_1[current_digit] = string_2[current_digit]
#     else:
#         continue
#     print("".join(string_1))


first_string = input()
second_string = input()
current_string = first_string

for i in range(len(current_string)):
    left_part = second_string[:i + 1]
    right_part = first_string[i + 1:]
    full_string = left_part + right_part
    if full_string == current_string:
        continue
    print(full_string)
    current_string = full_string
