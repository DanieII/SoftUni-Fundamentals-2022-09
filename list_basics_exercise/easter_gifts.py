lst_of_gifts = input().split()
OUT_OF_STOCK_COMMAND = "OutOfStock"
REQUIRED_COMMAND = "Required"
JUST_IN_CASE_COMMAND = "JustInCase"
command = input()
final_list = []
while command != "No Money":
    current_action = command.split()
    gift = current_action[1]
    if current_action[0] == OUT_OF_STOCK_COMMAND:
        if current_action[1] in lst_of_gifts:
            iterations = lst_of_gifts.count(gift)
            for i in range(iterations):
                current_index = lst_of_gifts.index(gift)
                lst_of_gifts[current_index] = "None"
    elif current_action[0] == REQUIRED_COMMAND:
        index_of_current_gift = int(current_action[2])
        if 0 <= index_of_current_gift < len(lst_of_gifts):
            lst_of_gifts[index_of_current_gift] = gift
    elif current_action[0] == JUST_IN_CASE_COMMAND:
        lst_of_gifts[-1] = gift
    command = input()
for i in range(len(lst_of_gifts)):
    if lst_of_gifts[i] != "None":
        final_list.append(lst_of_gifts[i])
print(" ".join(final_list))

