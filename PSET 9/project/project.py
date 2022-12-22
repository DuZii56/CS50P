import sys
import random


name = ""


#Randomize damage output
def damage():
    dmg = random.randint(1, 20)
    return dmg


class Character(object):
    def __init__(self, name, hp, dmg, potions=6):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.potions = potions
    #Function for attacking
    def attack(self, opponent):
        self.dmg = damage()
        opponent.hp = opponent.hp - self.dmg
    #Function for self-healing
    def heal(self, player):
        self.potions = self.potions - 1
        if self.potions > 1:
            player.hp = player.hp + 25
            if player.hp > 100:
                player.hp = 100
            print(
                f"""\nYour health is now {player.hp}.
                \nYou have {self.potions} potions."""
                )
        if self.potions == 1:
            player.hp = player.hp + 25
            if player.hp > 100:
                player.hp = 100
            print(
                f"""\nYour health is now {player.hp}.
                \nYou have {self.potions} potion."""
                )
        if self.potions == 0:
            print(
                f"""\nYour health is now {player.hp}.
                \nYou are out of potions!"""
                )


#Get the player's name
def get_name():
    global name
    try:
        name = input("\nWhat is your name? ")
        while name == '':
            TypeError(print("\nInvalid name"))
            name = input("What is your name? ")
    finally:
        return name


player = Character(get_name(), 100, int(damage()))
enemy = Character("Giant rubber duck", 150, int(damage()))


#Check if either character is alive
def alive(character):
    if character.hp > 0:
        return True
    if character.hp <= 0:
        return False


#Function for the enemy to attack
def battle():
    if alive(enemy):
        enemy.attack(player)
        print(f"\n{enemy.name} attacked {player.name} for {enemy.dmg} damage.")
        if alive(player) == False:
            print(f"\n{player.name} died.")
            sys.exit()
    if alive(enemy) == False:
        print(f"\n{player.name} killed {enemy.name}.")
        sys.exit()


#Main function, allows player to attack enemy or self-heal.
def main(player, enemy):
    saved_action = []
    fighting = True
    while fighting:
        while alive(player) and alive(enemy):
            if player.hp < 100:
                print (f"\n{player.name}'s health: {player.hp}")
                print (f"{enemy.name}'s health: {enemy.hp}")
                try:
                    action = input("Choose an action: attack or heal\n").lower()
                    if action == '':
                        action = saved_action
                    saved_action = action
                finally:
                    if action == "heal":
                        if player.potions == 0:
                            print("You are out of potions!  You have no choice but to attack.")
                            player.attack(enemy)
                            print(f"\n{player.name} attacked {enemy.name} for {player.dmg} damage.")
                            battle()
                        else:
                            player.heal(player)
                            battle()
                    if action == "attack":
                        player.attack(enemy)
                        print(f"\n{player.name} attacked {enemy.name} for {player.dmg} damage.")
                        battle()
            if player.hp >= 100:
                battle()


if __name__ == "__main__":
    main(player, enemy)
