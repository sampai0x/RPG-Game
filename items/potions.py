class Potion:
    def __init__(self, heal_amount):
        self.heal_amount = heal_amount

    def use(self, character):
        character.hp += self.heal_amount
        print(f"{character.name} usou uma poção e recuperou {self.heal_amount} HP!")
