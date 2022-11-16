import re

text = input()
pattern = re.compile('::[A-Z]{1}[a-z]{2,}::|\*{2}[A-Z]{1}[a-z]{2,}\*{2}')
found_emojis = re.findall(pattern, text)
# Find the cool threshold
cool_threshold = 1
for element in text:
    if element.isdigit():
        cool_threshold *= int(element)

# Deal with the cool emojis
cool_emojis = []
for emoji in found_emojis:
    current_coolness = 0
    for element in emoji:
        if element.isalpha():
            number = ord(element)
            current_coolness += number
    if current_coolness >= cool_threshold:
        cool_emojis.append(emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(found_emojis)} emojis found in the text. The cool ones are:")
[print(f"{x}") for x in cool_emojis]
