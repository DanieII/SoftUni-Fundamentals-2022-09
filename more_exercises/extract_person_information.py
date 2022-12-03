number_of_strings = int(input())
flag = False
for _ in range(number_of_strings):
    string = input()
    for symbol in string:
        if symbol == "@":
            name = ""
            for i in range(string.index("@") + 1, len(string)):
                if string[i] != "|":
                    name += string[i]
                else:
                    break
        elif symbol == "#":
            age = ""
            for i in range(string.index("#") + 1, len(string)):
                if string[i] != "*":
                    age += string[i]
                else:
                    Flag = True
                    break
        # The loop will stop because the name and age will be extracted from the string
        if flag:
            break
    print(f"{name} is {age} years old.")

# With regex
# import re
#
# pattern = r"@([A-Za-z]+)|#(\d+)*"
# number_of_strings = int(input())
# for _ in range(number_of_strings):
#     string = input()
#     result = re.findall(pattern, string)
#     name = result[0][0]
#     age = result[1][1]
#     print(f"{name} is {age} years old.")
