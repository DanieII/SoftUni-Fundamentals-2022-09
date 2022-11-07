words = input().replace(" ", "")
my_dict = {}
for letter in words:
    if letter not in my_dict:
        my_dict[letter] = 0
    my_dict[letter] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")
