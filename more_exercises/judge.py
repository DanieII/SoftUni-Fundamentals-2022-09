contests = {}
users = {}
command = input()
while command != "no more time":
    username, contest, points_as_str = command.split(" -> ")
    points = int(points_as_str)
    # Filling the contests
    if contest not in contests:
        contests[contest] = {username: points}
    elif username not in contests[contest]:
        # If there is a contest the current user has to be added to the contest
        contests[contest][username] = points
    else:
        # If the current user is already in the contest
        # we have to check if his points this time are more than before and if so replace the old points
        if contests[contest][username] < points:
            contests[contest][username] = points
    # Filling the users individual ratings
    if username not in users:
        users[username] = points
    else:
        if users[username] < points:
            # If there is a new submission with the same contest and the new points are more the old points are replaced
            users[username] = points
        else:
            users[username] += points

    command = input()
for k, v in contests.items():
    print(f"{k}: {len(v)} participants")
    scores_and_names_lst = []
    # Sorting names and scores in a list, so I can print them with enumerate easily
    # Minus in front of x means than it's going to be in descending order because by default it's ascending
    for name, score in sorted(v.items(), key=lambda x: (-x[1], x[0])):
        scores_and_names_lst.append(f"{name} <::> {score}")
    for i, s in enumerate(scores_and_names_lst):
        print(f"{i + 1}. {s}")
print("Individual standings:")
individual_scores_and_names_lst = []
for user, individual_score in sorted(users.items(), key=lambda x: (-x[1], x[0])):
    individual_scores_and_names_lst.append(f"{user} -> {individual_score}")
for index, string in enumerate(individual_scores_and_names_lst):
    print(f"{index + 1}. {string}")
