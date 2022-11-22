def check_in_individual(dict, name):
    if name in dict:
        return True


contests = {}
individual = {}
while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points_as_str = command.split(" -> ")
    points = int(points_as_str)

    if contest in contests:
        if username in contests[contest].keys():
            if points > contests[contest][username]:
                contests[contest][username] = points
        else:
            contests[contest][username] = points
    else:
        contests[contest] = {username: points}
for k, v in contests.items():
    for key, value in v.items():
        if key not in individual:
            individual[key] = value
        else:
            individual[key] += value

for k, v in contests.items():
    print(f"{k}: {len(v)} participants")
    scores_and_names_lst = []
    # Sorting names and scores in a list, so I can print them with enumerate easily
    for name, score in sorted(v.items(), key=lambda x: (-x[1], x[0])):
        scores_and_names_lst.append(f"{name} <::> {score}")
    for i, s in enumerate(scores_and_names_lst):
        print(f"{i + 1}. {s}")

print("Individual standings:")
individual_scores_and_names_lst = []
for user, individual_score in sorted(individual.items(), key=lambda x: (-x[1], x[0])):
    individual_scores_and_names_lst.append(f"{user} -> {individual_score}")
for index, string in enumerate(individual_scores_and_names_lst):
    print(f"{index + 1}. {string}")
