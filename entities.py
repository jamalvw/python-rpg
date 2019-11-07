class Entity:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage

class Player(Entity):
    def __init__(self, name: str, health: int, damage: int, items: list=[]):
        super(Player, self).__init__(name, health, damage)
        self.items = items