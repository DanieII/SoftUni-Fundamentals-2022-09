names = input().split(", ")
# sorting from the longest to the shortest and alphabetically
print(sorted(names, key=lambda x: (-len(x), x)))
