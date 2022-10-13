def loading_bar(percentage):
    if percentage == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    number_of_percentage_symbols = percentage // 10
    return f"""{percentage}% [{"%" * number_of_percentage_symbols}{"." * (10 - number_of_percentage_symbols)}]\nStill loading..."""


number = int(input())
print(loading_bar(number))
