from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)
player1 = Player("Grognak", "Dwarf", "Barbarian", 20, 130)
player2 = Player("Albus", "Elf", "Wizard", 40, 80)
player3 = Player("Bond", "Halfling", "Rogue", 10, 100)
player4 = Player("Batman", "Human", "Knight", 15, 150)
playerlist = [player1,player2,player3,player4]
# TODO: Create an instance of Weapon with random damage between 12 and 15
long_sword = Weapon("Excalibur", "Sword", 30)
cutlass = Weapon("Jack Sparrow's Cutlass", "Sword", 20)
axe = Weapon("EVH Guitar", "Axe", 25)
club = Weapon("The bat-bat", "club", 15)
weaponlist= [long_sword, cutlass, axe, club]
# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
goblin1 = Enemy("Foo Bar", "Goblin", 12, 50)

# Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")

# TODO: Print the player weapon details
print(f"Weapon Name: {long_sword.name}")
print(f"Weapon Category: {long_sword.category}")
print(f"Weapon Damage: {long_sword.damage}")

# TODO: Print the enemy character details
print(f"Enemy Name: {goblin1.name}")
print(f"Enemy Race: {goblin1.race}")
print(f"Enemy damage: {goblin1.damage}")
print(f"Enemy Health: {goblin1.health}")

ans = input("""Please choose your player character:
                1. Grognak
                2. Albus
                3. Bond
                4. Batman
                """)
ans = int(ans)
while 1<=ans>=4 :
    print("Invalid response")
    ans = input("""Please choose your player character:
                1. Grognak
                2. Albus
                3. Bond
                4. Batman
                """)
    ans = int(ans)

    
if ans == 1:
    user = player1
if ans == 2:
    user = player2
if ans == 3:
    user = player3
if ans == 4:
    user = player4

print(f"""You Chose {user.name}!
    Name: {user.name}
    Health: {user.health}
    Class: {user.cls}
    Race: {user.race}
    Damage: {user.atk}""")

ans = input("""Please choose your Weapon:
                1. Excalibur
                2. Jack Sparrow's Cutlass
                3. EVH Guitar
                4. The bat-bat
                """)
ans = int(ans)


while 1<=ans>=4 :
    print("Invalid response")
    ans = input("""Please choose your player character:
                1. Excalibur
                2. Jack Sparrow's Cutlass
                3. EVH Guitar
                4. The bat-bat
                """)
    ans = int(ans)

    
if ans == 1:
    wep = long_sword
if ans == 2:
    wep = cutlass
if ans == 3:
    wep = axe
if ans == 4:
    wep = club

print(f"""You Chose {wep.name}!
    Name: {wep.name}
    Category: {wep.category}
    Damage: {wep.damage}""")

