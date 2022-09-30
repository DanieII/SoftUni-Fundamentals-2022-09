number = list(input())
number.sort()
len_of_number = len(number)
for i in range(1, len_of_number + 1):
    print(number[-i], end="")
