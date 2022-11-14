def validation(string):
    if len(string) != 20:
        return "invalid ticket"
    left_side = string[:10]
    right_side = string[10:]
    winning_symbols = ['@', '#', '$', '^']
    for symbol in winning_symbols:
        for repetitions in range(10, 5, -1):
            if symbol * repetitions in left_side and symbol * repetitions in right_side:
                # If there is a jackpot
                if repetitions == 10:
                    return f'ticket "{string}" - {repetitions}{symbol} Jackpot!'
                # It's a winning ticket
                else:
                    return f'ticket "{string}" - {repetitions}{symbol}'
    # The ticket is valid but is not winning
    return f'ticket "{string}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(validation(ticket))
