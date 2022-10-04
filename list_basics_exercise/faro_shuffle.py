deck = input().split()
shuffled_deck = []
number_of_shuffles = int(input())
for _ in range(number_of_shuffles):
    first_side = deck[:len(deck) // 2]
    second_side = deck[len(deck) // 2:]
    deck = []
    for current_card in range(len(first_side)):
        deck.append(first_side[current_card])
        deck.append(second_side[current_card])
print(deck)
