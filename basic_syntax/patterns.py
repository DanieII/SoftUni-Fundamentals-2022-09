max_number = int(input())

for i in range(1, max_number + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print("")

for i in range(max_number - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print("")
