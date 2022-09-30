iterations = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_sum = 0
for i in range(iterations):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_sum = (current_weight / current_time) ** current_quality
    if current_sum > max_sum:
        max_sum = current_sum
        max_weight = current_weight
        max_time = current_time
        max_quality = current_quality
print(f"{max_weight} : {max_time} = {int(max_sum)} ({max_quality})")
