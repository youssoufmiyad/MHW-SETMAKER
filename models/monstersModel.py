class Monsters:
    def __init__(self):
        self.all = []


class Monster:
    def __init__(self, id, name, type, species, description, elements, ailments, locations, resistances, weaknesses, rewards):
        self.id = id
        self.name = name
        self.type = type
        self.species = species
        self.description = description
        self.elements = elements
        self.ailments = ailments
        self.locations = locations
        self.resistances = resistances
        self.weaknesses = weaknesses
        self.rewards = rewards

    def toString(self):
        return "Id : ", self.id, " Name : ", self.name, " Type : ", self.type, " Species : ", self.species, " Description : ", self.description, " Elements : ", self.elements, " Ailments : ", self.locations, " Resistances : ", self.resistances, " Weaknesses : ", self.weaknesses, " Rewards : ", self.rewards
