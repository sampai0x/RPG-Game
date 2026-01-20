from mechanics.dice import roll_dice

def attack(attacker, defender):
    dice = roll_dice()
    damage = attacker.attack + dice
    defender.take_damage(damage)

    print(f"{attacker.name} atacou {defender.name} causando {damage} de dano!")
    print(f"{defender.name} agora tem {defender.hp} HP \n")