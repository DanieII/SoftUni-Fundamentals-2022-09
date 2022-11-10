string_to_remove = input()
string = input()
while string_to_remove in string:
    string = string.replace(string_to_remove, "")
print(string)