string_of_money = input().split(", ")
number_of_beggars = int(input())
collected_sums = []
starting_index = 0
for _ in range(number_of_beggars):
    collected_money_for_current_beggar = 0
    for current_amount_index in range(starting_index, len(string_of_money), number_of_beggars):
        collected_money_for_current_beggar += int(string_of_money[current_amount_index])
    collected_sums.append(collected_money_for_current_beggar)
    starting_index += 1
print(collected_sums)
