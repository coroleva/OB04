from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def __init__ (self, name):
        self.name = name
    def attack(self):
        print(f"Боец выбрал {self.name} и атакует {self.name}")

class Bow(Weapon):
    def __init__ (self, name):
        self.name = name
    def attack(self):
        print(f"Боец выбрал {self.name} и атакует {self.name}")


class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def change_weapon(self, weapon: Weapon):
        print(f'боец выбрал новую вещь - {weapon.__class__.__name__}')
    def attack(self):
        self.weapon.attack()

swordsman = Fighter(Sword('Эскалибур'))
swordsman.attack()

bowman = Fighter(Bow('Арбалет'))
bowman.attack()


