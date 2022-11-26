import re

string = input()
pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
result = re.findall(pattern, string)
destinations = []
total_points = 0
for element in result:
    destination = element[1]
    destinations.append(destination)
    total_points += len(destination)
print("Destinations:", end=" ")
[print(x, end="") for x in ", ".join(destinations)]
print(f"\nTravel Points: {total_points}")
