import re

pattern_for_decryption = r"s|t|a|r"
number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []
for _ in range(number_of_messages):
    message = input()
    all_hidden_letters = re.finditer(pattern_for_decryption, message, re.I)
    # For every found letter increase the number variable by 1
    number = 0
    for _ in all_hidden_letters:
        number += 1
    # Decrypt the message
    decrypted_message = ""
    for element in message:
        decrypted_message += chr(ord(element) - number)
    pattern_for_validation = r"[^@\-!:>]*@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)"
    result = re.search(pattern_for_validation, decrypted_message)
    if result:
        name = result.group(1)
        attack_type = result.group(3)
        if attack_type == "A":
            attacked_planets.append(name)
        elif attack_type == "D":
            destroyed_planets.append(name)
# Attacked
if attacked_planets:
    print("Attacked planets:", len(attacked_planets))
    ordered_attacked_planets = sorted(attacked_planets, key=lambda x: x)
    for planet in ordered_attacked_planets:
        print(f"-> {planet}")
else:
    print("Attacked planets:", 0)
# Destroyed
if destroyed_planets:
    print("Destroyed planets:", len(destroyed_planets))
    ordered_destroyed_planets = sorted(destroyed_planets, key=lambda x: x)
    for planet in ordered_destroyed_planets:
        print(f"-> {planet}")
else:
    print("Destroyed planets:", 0)
