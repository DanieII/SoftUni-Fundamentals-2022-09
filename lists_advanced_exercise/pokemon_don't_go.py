distances = list(map(int, input().split()))
removed_elements = []

while len(distances) > 0:
    current_index = int(input())
    if current_index < 0:
        distance_to_add = distances.pop(0)
        distances.insert(0, distance_to_add)
        current_distance = distance_to_add
        removed_elements.append(distance_to_add)

    elif current_index > len(distances) - 1:
        distance_to_add = distances.pop()
        distances.append(distance_to_add)
        current_distance = distance_to_add
        removed_elements.append(distance_to_add)

    else:
        current_distance = distances[current_index]
        distances.remove(current_distance)
        removed_elements.append(current_distance)

    index = 0
    for distance in distances:
        if distance <= current_distance:
            distance += current_distance
            distances[index] = distance
        else:
            distance -= current_distance
            distances[index] = distance
        index += 1

print(sum(removed_elements))

# Judge 100/100
# distances = list(map(int, input().split()))
# removed = 0
#
# while len(distances) > 0:
#     current_index = int(input())
#     if 0 <= current_index < len(distances):
#         current_distance = distances.pop(current_index)
#
#     elif current_index < 0:
#         distance_to_add = distances[-1]
#         current_distance = distances[0]
#         distances[0] = distances[-1]
#
#     else:
#         distance_to_add = distances[0]
#         current_distance = distances[-1]
#         distances[-1] = distances[0]
#     removed += current_distance
#
#     for i, v in enumerate(distances):
#         if v <= current_distance:
#             distances[i] += current_distance
#         else:
#             distances[i] -= current_distance
#
# print(removed)
