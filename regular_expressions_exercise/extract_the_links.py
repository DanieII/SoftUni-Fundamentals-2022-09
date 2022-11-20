import re

pattern = r"(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)"
valid_links = []
while True:
    string = input()
    if not string:
        break

    result = re.search(pattern, string)
    if result:
        valid_links.append(result.group(0))
for link in valid_links:
    print(link)
