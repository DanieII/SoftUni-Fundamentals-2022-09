def integers(lst):
    lst_with_integers = list(map(int, lst))
    lst_with_strings = list(map(str, lst_with_integers))
    return ", ".join(lst_with_strings)


def closest(my_first, my_second):
    first_numbers_with_absolute_values = [abs(x) for x in my_first]
    second_numbers_with_absolute_values = [abs(x) for x in my_second]
    if first_numbers_with_absolute_values < second_numbers_with_absolute_values:
        return f"({integers(my_first)})"
    if first_numbers_with_absolute_values > second_numbers_with_absolute_values:
        return f"({integers(my_second)})"


first_coordinates = [float(input()), float(input())]
second_coordinates = [float(input()), float(input())]
print(closest(first_coordinates, second_coordinates))
