class Weapons:
    def __init__(self):
        self.all = []


class Weapon:

    def __init__(self, id,  name, type, rarity, attack, elements, crafting, assets,  damageType, attributes):
        self.id = id
        self.name = name
        self.type = type
        self.rarity = rarity
        self.attack = attack
        self.elements = elements
        self.crafting = crafting
        self.assets = assets
        self.damageType = damageType
        self.attributes = attributes

    def toString(self):
        return "Id : ", self.id, " Name : ", self.name, " Type : ", self.type, " Rarity : ", self.rarity, " Attack : ", self.attack, " Elements : ", self.elements, " Crafting : ", self.crafting, " Assets : ", self.assets, "Damage Type : ", self.damageType, " Attributes : ", self.attributes
