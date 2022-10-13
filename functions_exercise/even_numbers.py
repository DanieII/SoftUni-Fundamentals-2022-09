lst = input().split(" ")
lst_with_integers = [int(x) for x in lst]
final_list = filter(lambda x: x % 2 == 0, lst_with_integers)
print(list(final_list))
