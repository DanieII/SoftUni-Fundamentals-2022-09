contests_and_passwords = {}
users = {}
first_command = input()
while first_command != "end of contests":
    contest, password = first_command.split(":")
    contests_and_passwords[contest] = password
    first_command = input()

second_command = input()
while second_command != "end of submissions":
    access_contest, pas, name, points_as_str = second_command.split("=>")
    points = int(points_as_str)
    if access_contest in contests_and_passwords and contests_and_passwords[access_contest] == pas:
        if name not in users:
            users[name] = {access_contest: points}
        elif access_contest in users[name]:
            if users[name][access_contest] < points:
                users[name][access_contest] = points
        else:
            users[name][access_contest] = points
    second_command = input()
# Find the best student
best_score = 0
best_user = ""
for student, value in users.items():
    current_score = 0
    for score in value.values():
        current_score += score
    if current_score > best_score:
        best_user = student
        best_score = current_score
# Final print
print(f"Best candidate is {best_user} with total {best_score} points.")
print("Ranking:")
for student in sorted(users):
    print(student)
    for lesson, score in sorted(users[student].items(), key=lambda x: -x[1]):
        print(f"#  {lesson} -> {score}")
