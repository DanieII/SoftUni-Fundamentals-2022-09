all_words = list(map(lambda x: x.lower(), input().split()))
my_dict = {}
for word in all_words:
    if word not in my_dict:
        my_dict[word] = 0
    my_dict[word] += 1
for key in my_dict:
    if my_dict[key] % 2 != 0:
        print(key, end=" ")
