all_words = input().split()

deciphered_words = []

for word in all_words:
    number_as_string = ''
    current_word = []
    for current_letter in word:
        if current_letter.isdigit():
            number_as_string += current_letter
        else:
            current_word.append(current_letter)
    number_as_digits = int(number_as_string)
    # Inserting the string value of the number in front of the word
    current_word.insert(0, chr(number_as_digits))
    # Swapping the second and the last letter
    if len(current_word) > 2:
        current_word[1], current_word[-1] = current_word[-1], current_word[1]
    deciphered_words.append(''.join(current_word))

print(" ".join(deciphered_words))

#############################################################
# all_words = input().split()
# deciphered_words = []
# for word in all_words:
#     current_number_as_lst = [x for x in word if x.isdigit()]
#     current_word_as_lst = [x for x in word if x.isalpha()]
#     current_number = int("".join(current_number_as_lst))
#     current_word = "".join(current_word_as_lst)
#     full_word = chr(current_number) + current_word[::-1]
#     deciphered_words.append(full_word)
# print(" ".join(deciphered_words))
