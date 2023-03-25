import random

class Character:
    def __init__(self, name, class_type, hit_points, damage):
        self.name = name
        self.class_type = class_type
        self.hit_points = hit_points
        self.damage = damage

    def attack(self, target):
        target.hit_points -= self.damage

    def use_item(self, item):
        if isinstance(item, HealthPotion):
            self.hit_points += item.healing
            if self.hit_points > 100:
                self.hit_points = 100
        elif isinstance(item, ManaPotion):
            self.mana += item.restoration
            if self.mana > 50:
                self.mana = 50

class Wizard(Character):
    def __init__(self, name="Wizard", hit_points=50, damage=10):
        super().__init__(name, "Wizard", hit_points, damage)

class Warrior(Character):
    def __init__(self, name="Warrior", hit_points=100, damage=5):
        super().__init__(name, "Warrior", hit_points, damage)

class Rogue(Character):
    def __init__(self, name="Rogue", hit_points=75, damage=7):
        super().__init__(name, "Rogue", hit_points, damage)

class Barbarian(Character):
    def __init__(self, name="Barbarian", hit_points=150, damage=3):
        super().__init__(name, "Barbarian", hit_points, damage)

class Ranger(Character):
    def __init__(self, name="Ranger", hit_points=80, damage=8):
        super().__init__(name, "Ranger", hit_points, damage)

class Item:
    def __init__(self, name):
        self.name = name

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion")
        self.healing = 20

class ManaPotion(Item):
    def __init__(self):
        super().__init__("Mana Potion")
        self.restoration = 10

class Monster:
    def __init__(self, name, hit_points, damage):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage

    def attack(self, target):
        target.hit_points -= self.damage

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 20, 5)

class Rat(Monster):
    def __init__(self):
        super().__init__("Rat", 10, 3)

class Spider(Monster):
    def __init__(self):
        super().__init__("Spider", 15, 4)

class Brutallus(Monster):
    def __init__(self):
        super().__init__("Brutallus", 100, 10)

print("Welcome to the game!")

# Prompt the player to select a character class
print("Select a character class:")
print("1. Wizard")
print("2. Warrior")
print("3. Rogue")
print("4. Barbarian")
print("5. Ranger")
class_choice = int(input("Enter a number between 1 and 5: "))

# Create the player's character based on their choice
if class_choice == 1:
    player = Wizard()
elif class_choice == 2:
    player = Warrior()
elif class_choice == 3:
    player = Rogue()
elif class_choice == 4:
    player = Barbarian()
elif class_choice == 5:
    player = Ranger()
else:
    raise Exception("Invalid character class choice")

print(f"You have selected a {player.class_type}.")

# Create some monsters for the player to fight
monsters = [Goblin(), Rat(), Spider()]

# Create a boss monster
boss = Brutallus()

# Start the game loop
game_over = False
while not game_over:
    # Print the player's status
    print(f"{player.name}: {player.hit_points} HP")

    # Prompt the player to take an action
    print("Select an action:")
    print("1. Attack")
    print("2. Use item")
    action_choice = int(input("Enter a number between 1 and 2: "))

    if action_choice == 1:
        # Select a random monster to attack
        target = random.choice(monsters)
        print(f"You attack the {target.name}!")
        player.attack(target)
        if target.hit_points <= 0:
            print(f"You defeated the {target.name}!")
            monsters.remove(target)
            if not monsters:
                print("Congratulations, you have won the game!")
                game_over = True
    elif action_choice == 2:
        # Allow the player to use an item
        print("Select an item to use:")
        print("1. Health Potion")
        print("2. Mana Potion")
        item_choice = int(input("Enter a number between 1 and 2: "))

        if item_choice == 1:
            item = HealthPotion()
            player.use_item(item)
            print(f"You use a {item.name} and gain {item.healing} HP.")
        elif item_choice == 2:
            item = ManaPotion()
            player.use_item(item)
            print(f"You use a {item.name} and gain {item.restoration} mana.")

    # If there are no more monsters, spawn the boss
    if not monsters and not game_over:
        print("You have defeated all the monsters. The boss has appeared!")
        target = boss

    # Allow the boss to attack
    if isinstance(target, Brutallus):
        target.attack(player)
        print(f"The boss attacks you and deals {target.damage} damage.")
        if player.hit_points <= 0:
            print("Game over. You have been defeated by the boss.")
            game_over = True
    else:
        # Select a random monster to attack the player
        monster = random.choice(monsters)
        monster.attack(player)
        print(f"The {monster.name} attacks you and deals {monster.damage} damage.")
        if player.hit_points <= 0:
            print("Game over. You have been defeated by a monster.")
            game_over = True

