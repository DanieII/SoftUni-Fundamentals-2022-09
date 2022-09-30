number_of_words_detected = 0
word = input().lower()
key_words = ["sand", "water", "fish", "sun"]
for current_word in range(len(key_words)):
    number_of_words_detected += word.count(key_words[current_word])
print(number_of_words_detected)
