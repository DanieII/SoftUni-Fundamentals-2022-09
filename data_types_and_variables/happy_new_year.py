year = int(input())
happy_year = False

while not happy_year:
    year += 1
    digits_set = set()
    for i in range(len(str(year))):
        digits_set.add(str(year)[i])
    if len(digits_set) == len(str(year)):
        happy_year = True
print(year)
