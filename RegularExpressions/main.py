class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        new_list = [i for i in self.products if i[0] == letter]
        return new_list

    def __repr__(self):
        self.products.sort()
        string = '\n'.join(self.products)
        return f"Items in the {self.name} catalogue:\n{string}"


#To save time:
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)