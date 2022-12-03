start = ord(input())
end = ord(input())
string = input()
valid = []
for symbol in string:
    current_value = ord(symbol)
    if start < current_value < end:
        valid.append(current_value)
print(sum(valid))
