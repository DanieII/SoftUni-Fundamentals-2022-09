import re

number_of_iterations = int(input())
pattern = r"\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+"
for _ in range(number_of_iterations):
    string = input()
    result = re.match(pattern, string)
    # If it has a value
    if result:
        product_group = "".join([x for x in string if x.isdigit()])
        if not product_group:  # if len(product_group) == 0:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
