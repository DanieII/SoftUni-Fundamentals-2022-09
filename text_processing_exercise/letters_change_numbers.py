string = input().split()
final_sum = 0
for word in string:
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:-1])

    if first_letter.isupper():
        number /= (ord(first_letter) - 64)
    elif first_letter.islower():
        number *= (ord(first_letter) - 96)

    if last_letter.isupper():
        number -= (ord(last_letter) - 64)
    elif last_letter.islower():
        number += (ord(last_letter) - 96)
    final_sum += number
print(f"{final_sum:.2f}")
