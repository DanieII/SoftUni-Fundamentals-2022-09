number_of_pieces = int(input())
pieces = {}
for _ in range(number_of_pieces):
    initial_piece, initial_composer, initial_key = input().split("|")
    pieces[initial_piece] = [initial_composer, initial_key]
while True:
    command = input()
    if command == "Stop":
        break

    split = command.split("|")
    action = split[0]
    piece = split[1]
    if action == "Add":
        composer, key = split[2], split[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
            continue
        pieces[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            continue
        del pieces[piece]
        print(f"Successfully removed {piece}!")
    elif action == "ChangeKey":
        key = split[2]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            continue
        pieces[piece][1] = key
        print(f"Changed the key of {piece} to {key}!")
for k, v in pieces.items():
    print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")
