key = [int(x) for x in input().split()]
while True:
    command = input()
    if command == "find":
        break

    string = command
    key_number = 0
    decrypted_message = ""
    flag = False
    for symbol in string:
        if key_number > len(key) - 1:
            key_number = 0
        new_symbol = chr(ord(symbol) - key[key_number])
        decrypted_message += new_symbol
        key_number += 1
    for letter in decrypted_message:
        if letter == "&":
            treasure_type = ""
            for i in range(decrypted_message.index("&") + 1, len(decrypted_message)):
                if decrypted_message[i] != "&":
                    treasure_type += decrypted_message[i]
                else:
                    break
        elif letter == "<":
            coordinates = ""
            for j in range(decrypted_message.index("<") + 1, len(decrypted_message)):
                if decrypted_message[j] != ">":
                    coordinates += decrypted_message[j]
                else:
                    Flag = True
                    break
        if flag:
            break
    print(f"Found {treasure_type} at {coordinates}")
