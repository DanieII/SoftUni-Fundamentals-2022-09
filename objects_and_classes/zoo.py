class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, current_species, name):
        self.current_species = current_species
        self.name = name
        if self.current_species == "mammal":
            self.mammals.append(self.name)
        elif self.current_species == "fish":
            self.fishes.append(self.name)
        elif self.current_species == "bird":
            self.birds.append(self.name)
        Zoo.__animals += 1

    def get_info(self, species):
        self.species = species
        self.names = []
        if self.species == "mammal":
            self.names = ", ".join(self.mammals)
            return f"Mammals in {self.zoo_name}: {self.names}\nTotal animals: {Zoo.__animals}"
        elif self.species == "fish":
            self.names = ", ".join(self.fishes)
            return f"Fishes in {self.zoo_name}: {self.names}\nTotal animals: {Zoo.__animals}"
        elif self.species == "bird":
            self.names = ", ".join(self.birds)
            return f"Birds in {self.zoo_name}: {self.names}\nTotal animals: {Zoo.__animals}"


zoo = Zoo(input())
iterations = int(input())
for _ in range(iterations):
    species, name = input().split()
    zoo.add_animal(species, name)
species_to_print = input()
print(zoo.get_info(species_to_print))
