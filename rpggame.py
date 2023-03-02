# To do: Make class for "Hero" character.
# To do: Implement random function for a minigame.
# To do: Add spaces between paragraphs.

class Hero:
    def __init__(self, name, hp, damage, mana):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana

    def get_hp(self):
        return self.hp

    def get_damage(self):
        return self.damage

    def get_mana(self):
        return self.mana


class Mage(Hero):
    def __init__(self, name, hp, damage, mana, spell):
        super().__init__(name, hp, damage, mana)
        self.spell = "Fireball"


rogue = "Rogue"
paladin = "Paladin"
warrior = "Warrior"
mage = "Mage"
archer = "Archer"

rogue_hp = 200
archer_hp = 200
paladin_hp = 300
warrior_hp = 300
mage_hp = 150

inventory = []

print("***Ryan's Fantasy RPG Game***")
print("You walk along a bumpy cobblestone road, it is a foggy morning with the sun just shining through the fog. You smell thick smoke in the air, and you hear the distant sound of army orders and siege engines in the distance...")
print("It has been three days since you escaped from Castle Cerys in the Kingdom of Cyrillon. The Castellan sent for you this morning and handed you a letter from the King himself. The letter requests aid from the neighboring kingdom of Aeterna, for the castle is being sieged by Imperial forces..")
print("You have been tasked with delivering the letter to the King of Aeterna. First however, you must cross the treacherous Enchanted Forest which lies in your way.")
input("Press Enter to continue...")
print("\nTo get started, please create your character.")
print("| Warrior | Paladin | Mage | Rogue | Archer |")
playerclass = input("Choose your class:")
while True:
    if playerclass == "warrior" or playerclass == "Warrior":
        charclass = warrior
        charhp = warrior_hp
        print(f"You have chosen a Warrior.")
        print(f"Your HP is: {charhp}.")
        break
    elif playerclass == "Paladin" or playerclass == "paladin":
        charclass = paladin
        charhp = paladin_hp
        print(f"You have chosen a Paladin.")
        print(f"Your HP is {charhp}")
        break
    elif playerclass == "Mage" or playerclass == "mage":
        charclass = mage
        charhp = mage_hp
        print("You have chosen a Mage.")
        print(f"Your HP is {charhp}")
        break
    elif playerclass == "Archer" or playerclass == "archer":
        charclass = archer
        charhp = archer_hp
        print("You have chosen an Archer.")
        print(f"Your HP is: {charhp}")
        break
    elif playerclass == "Rogue" or playerclass == "rogue":
        charclass = rogue
        charhp = rogue_hp
        print("You have chosen a Rogue.")
        print(f"Your HP is: {charhp}")
        break
    else:
        print("Please make a valid selection.")

while True:
    charname = input("Give your character a name:")
    if len(charname) < 1 or len(charname) > 10:
        print("Please enter a name between 1-10 characters")
    else:
        print(f"Your name is: {charname}")
        break

while True:
    print("Races: Human | Elf | Dwarf | Halfling")
    races = ["Human", "Elf", "Dwarf", "Halfling"]
    charrace = input("Please choose your character's race:")
    if charrace in races:
        print(f"You have chosen {charrace}")
        print(f"You are a {charrace} {charclass} named {charname}")
        break
    else:
        print("Please choose a valid selection.")

print("\n You approach the entrance of the forest from the road, it is separated from the road by a small clearing of felled land.")
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
        f"Goblin: King? Kingdom? War? You think I care about your petty {charrace} problems?")
    print("Goblin: Now, before I get angry, hand over everything you've got!")