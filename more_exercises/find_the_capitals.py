capital_letters = []
string = input()
current_index = 0
for i in string:
    if i.isupper():
        capital_letters.append(current_index)
    current_index += 1
print(capital_letters)
