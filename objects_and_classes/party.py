class Party:

    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def total(self):
        return len(self.people)

    def all_people(self):
        return ", ".join(self.people)


party = Party()

name = input()
while name != "End":
    party.invite(name)
    name = input()

print(f"Going: {party.all_people()}")
print(f"Total: {party.total()}")
