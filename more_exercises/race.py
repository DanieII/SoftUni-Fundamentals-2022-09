import re

# the first input are the names
racers = {x: 0 for x in input().split(", ")}
# First group stores all the letters and second is for the digits
pattern_for_name = r"([A-Za-z]+)"
pattern_for_distance = r"(\d)"
while True:
    command = input()
    if command == "end of race":
        break

    name = "".join(re.findall(pattern_for_name, command))
    distance_as_str = (re.findall(pattern_for_distance, command))
    distance = sum([int(x) for x in distance_as_str])
    if name in racers.keys():
        racers[name] += distance
ordered_racers = dict(sorted(racers.items(), key=lambda x: x[1], reverse=True))
places = ["1st", "2nd", "3rd"]
current_place = 1
for racer in ordered_racers:
    if current_place <= 3:
        print(f"{places[current_place - 1]} place: {racer}")
        current_place += 1
# A comprehension idea that doesn't work because of the suffix
# [print(f"{i}{suffix} place: {v}") for i, v in enumerate(ordered_racers.items()) for suffix in ["st", "nd", "rd"]]
