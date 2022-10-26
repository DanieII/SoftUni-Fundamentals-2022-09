first_lst = input().split(", ")
second_lst = input().split(", ")
substrings = []
for first_string in first_lst:
    for second_string in second_lst:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)
