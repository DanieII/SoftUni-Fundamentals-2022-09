class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.given_letter_lst = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        for word in self.products:
            if word.startswith(first_letter):
                self.given_letter_lst.append(word)
        return self.given_letter_lst

    def __repr__(self):
        second_part = "\n".join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n" + second_part

# TEST
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
