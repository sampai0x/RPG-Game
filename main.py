from characters.hero import Hero
from characters.monster import Monster
from mechanics.combat import attack
from items.potions import Potion

def main():
    hero = Hero("Arthur", hp=100, attack=10)
    monster = Monster("Goblin", hp=60, attack=8)
    potion = Potion(20)

    print("⚔️ Batalha iniciada!\n")

    while hero.is_alive() and monster.is_alive():
        attack(hero, monster)

        if monster.is_alive():
            attack(monster, hero)

        if hero.hp <= 40:
            potion.use(hero)

    if hero.is_alive():
        print("🏆 O herói venceu!")
    else:
        print("💀 O monstro venceu!")

if __name__ == "__main__":
    main()
