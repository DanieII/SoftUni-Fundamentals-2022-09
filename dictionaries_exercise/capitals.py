countries = input().split(", ")
capitals = input().split(", ")
my_dict = {country: capital for country, capital in zip(countries, capitals)}
for element in my_dict:
    capital = my_dict[element]
    print(f"{element} -> {capital}")
