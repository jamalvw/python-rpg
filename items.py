from entities import Entity
from abc import abstractmethod

class Item:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def use(self, entity: Entity) -> str:
        pass

class Potion(Item):
    def __init__(self, value: int):
        super(Potion, self).__init__("Potion")
        self.value = value

    def use(self, entity: Entity) -> str:
        entity.health += self.value
        return entity.name + ": " + str(entity.health)