class Sets:
    def __init__(self):
        self.all = []


class Set:

    def __init__(self, id,  name, rank, pieces, bonus):
        self.id = id
        self.name = name
        self.rank = rank
        self.pieces = pieces
        self.bonus = bonus
        
    def toString(self):
        return "Id : ", self.id, " Name : ", self.name, " Rank : ", self.rank, " Pieces : ", self.pieces, " Bonus : ", self.bonus
