string = input()
strength = 0
final = ""
for index in range(len(string)):
    if string[index] == ">":
        strength += int(string[index + 1])
        final += ">"
    # If the current element is not an explosion symbol and there still is strength the element should explode
    elif strength > 0 and string[index] != ">":
        strength -= 1
    else:
        final += string[index]
print(final)
