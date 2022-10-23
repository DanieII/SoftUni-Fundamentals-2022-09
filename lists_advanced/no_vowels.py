def no_vowels(my_text):
    new_string = [current_letter for current_letter in my_text if current_letter.lower() not in vowels]
    final_output = "".join(new_string)
    return final_output


vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
print(no_vowels(text))
