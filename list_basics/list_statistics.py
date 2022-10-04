iterations = int(input())
positives = []
negatives = []
for numbers in range(iterations):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)
print(f"{positives}")
print(f"{negatives}")
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
