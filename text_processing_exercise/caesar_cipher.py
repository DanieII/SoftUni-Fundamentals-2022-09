starting_string = input()
final = ""
for element in starting_string:
    final += chr(ord(element) + 3)
print(final)
