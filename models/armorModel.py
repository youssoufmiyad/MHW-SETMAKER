import json
class Armors:
    def __init__(self):
        self.all = []


class Armor:

    def __init__(self, id,  name, rank, pieces, bonus):
        self.id = id
        self.name = name
        self.rank = rank
        self.pieces = pieces
        self.bonus = bonus

    def toString(self):
        return "Id : ", self.id, " Name : ", self.name, " Rank : ", self.rank, " Pieces : ", self.pieces, " Bonus : ", self.bonus

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False))