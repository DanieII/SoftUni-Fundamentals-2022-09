number_of_electrons = int(input())
lst_of_all_shells = []
current_shell = 1
while True:
    current_max = 2 * current_shell ** 2
    current_shell += 1
    if number_of_electrons - current_max >= 0:
        number_of_electrons -= current_max
        lst_of_all_shells.append(current_max)
    # In case current shell's max is more than the electrons left
    else:
        current_max = number_of_electrons
        lst_of_all_shells.append(current_max)
        break

print(lst_of_all_shells)
