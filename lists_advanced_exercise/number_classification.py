def positive_numbers(numbers):
    return [x for x in numbers if x >= 0]


def negative_numbers(numbers):
    return [x for x in numbers if x < 0]


def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]


def odd_numbers(numbers):
    return [x for x in numbers if x % 2 != 0]


all_numbers = list(map(int, input().split(", ")))
print(f"""Positive: {", ".join(list(map(str, positive_numbers(all_numbers))))}
Negative: {", ".join(list(map(str, negative_numbers(all_numbers))))}
Even: {", ".join(list(map(str, even_numbers(all_numbers))))}
Odd: {", ".join(list(map(str, odd_numbers(all_numbers))))}
""")
