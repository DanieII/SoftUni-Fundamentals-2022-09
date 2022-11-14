string = input()
final = ''
last = ''
for letter in string:
    if letter != last:
        last = letter
        final += letter
print(final)



# Works if a sequence with the same letter is not repeated twice or more
# string = input()
# final = ""
# for letter in string:
#     if letter not in final:
#         final += letter
# print(final)
