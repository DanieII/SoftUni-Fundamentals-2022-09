version = list(map(int, input().split(".")))
for current_index in range(len(version) - 1, -1, -1):
    if version[current_index] + 1 <= 9:
        version[current_index] += 1
        break
    version[current_index] = 0
print(".".join(map(str, version)))
