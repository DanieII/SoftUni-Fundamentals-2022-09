iterations = int(input())
my_dict = {}
for _ in range(iterations):
    word = input()
    synonym = input()
    if word not in my_dict:
        my_dict[word] = []
    my_dict[word].append(synonym)
for key, value in my_dict.items():
    synonyms = ", ".join(value)
    print(f"{key} - {synonyms}")
