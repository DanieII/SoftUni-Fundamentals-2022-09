class Inventory:
    def __init__(self, __capacity):
        self.items = []
        self.capacity = __capacity

    def add_item(self, item: str):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        left_capacity = self.capacity - len(self.items)
        items = ", ".join(self.items)
        return f"Items: {items}.\nCapacity left: {left_capacity}"

# TEST
# inventory = Inventory(2)
# inventory.add_item("potion")
# inventory.add_item("sword")
# print(inventory.add_item("bottle"))
# print(inventory.get_capacity())
# print(inventory)
