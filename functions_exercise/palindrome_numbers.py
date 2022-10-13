def palindrome(my_number):
    for current_number in my_number:
        reversed_number = current_number[::-1]
        if current_number == reversed_number:
            print("True")
        else:
            print("False")


lst_of_numbers = input().split(", ")
palindrome(lst_of_numbers)
