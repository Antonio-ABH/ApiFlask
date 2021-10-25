class Card:
    def __init__(self, attack : int, defense : int):
        self.attack = attack
        self.defense = defense

class Player:
    def __init__(self, id : int, name : str, score : float):
        self.id = id
        self.name = name
        self.score = score

class Parameter:
    def __init__(self, attribute : str, value : str):
        self.attribute = attribute
        self.value = value