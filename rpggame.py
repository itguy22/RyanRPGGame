# Paladin characters (near end of game, after encounter with Sorcerer)

# Sorcerer character (near end of game)

import random


class Hero:
    def __init__(self, name, health, mana, strength, agility, intelligence, level=1, exp=0):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.level = level
        self.exp = exp

    def attack(self, target):
        damage = self.strength * 2
        target.receive_damage(damage)

    def receive_damage(self, damage):
        self.health -= damage

    def use_mana(self, amount):
        if amount <= self.mana:
            self.mana -= amount
            return True
        else:
            return False

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100 * self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.health += 10
        self.mana += 5
        self.strength += 2
        self.agility += 2
        self.intelligence += 2
        print(f"{self.name} leveled up to level {self.level}!")


def create_hero():
    name = input("Enter your hero's name: ")
    health = 100
    mana = 50
    strength = 10
    agility = 20
    intelligence = 30
    return Hero(name, health, mana, strength, agility, intelligence)


class Enemy:
    def __init__(self, name, health, mana, strength, agility, intelligence):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def attack(self, target):
        damage = self.strength * 2
        target.receive_damage(damage)

    def receive_damage(self, damage):
        self.health -= damage

    def use_mana(self, amount):
        if amount <= self.mana:
            self.mana -= amount
            return True
        else:
            return False


def battle(hero, enemy):
    while hero.health > 0 and enemy.health > 0:
        # Hero's turn
        print(hero.name + "'s turn!")
        hero.attack(enemy)
        print(enemy.name + " received " + str(hero.strength * 2) + " damage!")
        if enemy.health <= 0:
            print(enemy.name + " has been defeated!")
            break

        # Prompt player to attack
        input("Press enter to continue...")

        # Enemy's turn
        print(enemy.name + "'s turn!")
        enemy.attack(hero)
        print(hero.name + " received " + str(enemy.strength * 2) + " damage!")
        if hero.health <= 0:
            print(hero.name + " has been defeated!")
            break

        # Prompt player to attack
        input("Press enter to continue...")

    print("The battle is over.")


def select_class():
    print("Please select a character class: ")
    classes = ["Warrior", "Paladin", "Rogue", "Archer", "Mage"]
    for i, class_name in enumerate(classes):
        print(f"{i+1}. {class_name}")
    while True:
        try:
            class_index = int(
                input("Enter the number of the class you want to select: "))
            if class_index < 1 or class_index > len(classes):
                raise ValueError
            else:
                return classes[class_index - 1]
        except ValueError:
            print("Invalid input. Please enter a valid class number.")


def select_race():
    races = ['Human', 'Elf', 'Dwarf', 'Halfling']
    while True:
        print('Please select your race: ')
        for i, race in enumerate(races):
            print(f'{i + 1}. {race}')
        choice = input('Enter your choice (1-4): ')
        if choice.isdigit() and int(choice) in range(1, 5):
            return races[int(choice) - 1]
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Potion(Item):
    def __init__(self, name, description, potion_type, amount):
        super().__init__(name, description)
        self.potion_type = potion_type
        self.amount = amount

    def use(self, character):
        if self.potion_type == "health":
            character.health += self.amount
            print(f"{character.name} gained {self.amount} health.")
        elif self.potion_type == "mana":
            character.mana += self.amount
            print(f"{character.name} gained {self.amount} mana.")


class Character:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Mana: {self.mana}"


health_potion = Potion(
    "Health Potion", "Restores 20 health points", "health", 20)
mana_potion = Potion("Mana Potion", "Restores 10 mana points", "mana", 10)

player_hero = create_hero()
print(f"Welcome {player_hero.name}!")

player_class = select_class()
print(f"You have selected the {player_class} class!")

my_enemy = Enemy("Goblin", 50, 0, 8, 12, 5)

player_race = select_race()
print(f"You have chosen to be a {player_race}")


def roll_dice_to_escape():
    escape_chance = 50  # Percentage chance to escape
    player_roll = random.randint(1, 100)  # Roll a 100-sided dice

    if player_roll <= escape_chance:
        print("You successfully escaped the battle!")
        return True
    else:
        print("You failed to escape the battle. Prepare to fight!")
        return False


# my_enemy.attack(player_hero)

inventory = []

print("***Ryan's Fantasy RPG Game***")
print("You walk along a bumpy cobblestone road, it is a foggy morning with the sun just shining through the fog. You smell thick smoke in the air, and you hear the distant sound of army orders and siege engines in the distance...")
print("It has been three days since you escaped from Castle Cerys in the Kingdom of Cyrillon. The Castellan sent for you this morning and handed you a letter from the King himself. The letter requests aid from the neighboring Kingdom of Aeterna,  for the castle is being sieged by Imperial forces..")
print("You have been tasked with delivering the letter to the King of Aeterna. First however, you must cross the treacherous Enchanted Forest which lies in your way.")
input("Press Enter to continue...")

print("\nYou approach the entrance of the forest from the road, it is separated from the road by a small clearing of felled land.")
print("You enter the forest, as soon as you enter the trees start to close in around you and it grows darker, much darker. You hear a crow call out from deeper in the woods.")
print("It is just beginning to turn to dusk, as you walk leaves crunch softly under your boots.")
input("Press Enter to Continue...")

print("As you are walking through the forest, you approach a small clearing. In the center of the clearing, you see an unlit fire. Surrounding the fire are some woolen blankets and bedrolls.")
print("You approach the fire and tents, it looks as though there are just a few sparks of flame left in the fire. There is a teapot nearby, you touch it, it is cold to the touch.")
print("1. Investigate the area further.")
print("2. Leave the area.")
decision1 = input("Pick an option...")

while True:
    if decision1 == "1":
        print("\nYou decide to investigate the area further. You take a look inside the tent closest to you, inside you see an unfurled bedroll and a broken lamp.")
        print("You look around the campsite, on the other end of the fire you see a small wooden crate.")
        print("You approach the crate and open it")
        print("Inside the crate you find a Rusty Dagger and an Apple.")
        print("Rusty Dagger and Apple have been added to your inventory.")
        inventory.append("Rusty Dagger")
        inventory.append("Apple")
        print(f"Inventory: {inventory}")
        print("You close the crate and leave the area.")
        break
    if decision1 == "2":
        print("You leave the area and move on.")
        break

print("\nYou continue traversing through the forest, you are travelling North towards the Kingdom of Aeterna.")
print("As you walk, the wind starts to pick up, and you feel the air changing. It is about to start raining...")
print("Up ahead, you hear a rustling in the bush. You look in the direction you heard the noise, but see nothing.")
print("Then, all of a sudden, a Goblin hops out of the bush!")
print("The Goblin giggles mischievously and yells: Give me all your gold!")
print("What do you do?")
print("1. Try to talk to the Goblin, 2. Fight the goblin, 3. Attempt to run away")
decision2 = input("Pick an option...")
if decision2 == "1":
    print("You try to reason with the Goblin, telling him that you're on an important mission from the King of Lyrica and to leave you alone.")
    print(
        f"Goblin: King? Kingdom? War? You think I care about your petty {player_race} problems?")
    print("Goblin: Now, before I get angry, hand over everything you've got!")
    print("The Goblin pulls out a dagger from his boot and charges you!")
    battle(player_hero, my_enemy)
    player_hero.gain_exp(50)
if decision2 == "2":
    print("You draw your weapon, ready to attack the Goblin.")
    print("Goblin: What's this? A fight? You won't stand a chance!")
    print("The Goblin pulls out a dagger from his boot and charges you!")
    battle(player_hero, my_enemy)
    player_hero.gain_exp(50)
elif decision2 == "3":
    print("You attempt to run away from the Goblin.")
    if __name__ == "__main__":
        ESCAPED = roll_dice_to_escape()
        if not ESCAPED:
            # Continue with the battle logic against the NPC
            pass
battle(player_hero, my_enemy)
print("You loot a Health Potion from the Goblin.")
print("Health Potion has been added to your inventory.")
inventory.append("Health Potion")
print("You start walking again as night falls over the forest.")
print("It grows colder as night sets in, and the clouds gather, it starts raining...")
print("The cold chills you to the bone, you keep walking and see nothing for a while, then in the distance you spot a small clearing and a road running through it.")
print("You can just barely make things out on the road, but it looks like there's an upturned cart up ahead. You can see a figure, human-height standing next to it.")
print("What will you do?")
print("1. Approach the cart. 2. Continue walking.")
decision3 = input("Pick an option...")
if decision3 == "1":
    print("You start walking towards the cart, as you approach it you see that it is a man standing next to the cart. He appears to be frustrated.")
    print("You walk up to the man and greet him.")
    print("The man looks up, surprised to see anyone else in the middle of nowhere. He greets you.")
    print("Man: Hello stranger, I'm glad to see someone else out here. My cart broke down, i've been out here since daybreak.")
    print("You look at the cart, and notice that the wheels are bent at an angle and broken.")
    print("Stranger: I'm a merchant from the Kingdom of Cyrillon, I was on my way to the Kingdom of Aeterna when my cart's wheel got stuck in the mud and broke.")
    print("Will you help me fix it? I don't have much with me but I can give you a reward.")
    print("1. Yes, I will help you. 2. No, I'm in a hurry. 3. Draw your weapon.")
    decision4 = input("Pick an option...")
    if decision4 == "1":
        print("Stranger: Thank you! Here, please hold the wheel while I try to repair it.")
        print("You hold the wheel while the stranger fixes it. While you are holding it, you notice that there are some arrows stuck in the cart.")
        print("The man finishes fixing the wheel.")
        print("Stranger: Thank you for your help, I don't know if I would have been able to fix it on my own. The name's Alex, what's yours?")
        print("You tell him your name.")