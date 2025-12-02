import random 
import time

print("WELCOME TO BATTLE!")
time.sleep(1)
print("In this world, warriors from distant lands")
print("clash in deadly duels to prove their strength.")
time.sleep(2)
print("\nArchers, Vikings, Illusionists, King, Samurais, Hercules...")
print("Each fighter has unique skills and deadly attacks.")
time.sleep(2)
print("\nChoose your champion, face your enemy...")
time.sleep(1.5)
print("And may the strongest warrior survive.")
time.sleep(2)

print("LET THE BATTLE BEGIN")
time.sleep(1.5)

#heres everything our player have
class Fighter:
    def __init__ (self, name, hp, attack, defense, dodge, crit, abilities, defense_name):
        self.name = name #our name
        self.hp = hp #our health
        self.attack = attack 
        self.defense = defense 
        self.dodge = dodge 
        self.crit = crit
        self.abilities = abilities
        self.defense_name = defense_name 

#just checking if we're alive or no
    def is_alive(self):
        return self.hp > 0
    
    #damage and how we take it
    def take_damage(self, dmg):
        if random.randint(1, 100) <= self.dodge:
            print(f'{self.name} dodged!')
            return 0
        
        dmg = max(0, dmg - self.defense)
        self.hp -= dmg
        return dmg
    
#regular attack
    def normal_attack(self):
        dmg = random.randint(self.attack - 3, self.attack + 3)
        if random.randint(1, 100) <= self.crit:
            dmg *= 2
            print('fatal blow!')
        return dmg
    
#my fav part, basically we give a choice to a player, just for variety
#first is archer and every each of the characters have their own attack techniques
def archer_attack(choice, player):
    if choice == 'arrow shot':
        return random.randint(player.attack + 5, player.attack + 10)
    if choice == 'bow strike':
        return random.randint(player.attack + 3, player.attack +8)
    if choice == 'knee strike':
        return random.randint(player.attack + 4, player.attack +9)
    return None #shout out to gpt because game just didnt work without this, it helps me to not show anything if i mispell attack

#next one is viking
def viking_attack(choice, player):
    if choice == 'axe throw':
        return random.randint(player.attack + 6, player.attack + 12)
    if choice == 'overhead axe swing':
        return random.randint(player.attack + 7, player.attack + 14)
    if choice == 'shoulder bash':
        return random.randint(player.attack + 5, player.attack + 10)
    return None

#added this one cause witch doesnt sound as cool
def illusionist_attack(choice, player):
    if choice == 'illusionary projectile':
        return random.randint(player.attack + 4, player.attack + 9)
    if choice == 'ethereal blade':
        return random.randint(player.attack + 5, player.attack +12)
    if choice == 'mind shock':
        return random.randint(player.attack + 3, player.attack + 8)
    return None

#heres THE king
def king_attack(choice, player):
    if choice == 'royal decree':
        return random.randint(player.attack + 6, player.attack + 12)
    if choice == 'sword strike':
        return random.randint(player.attack + 5, player.attack +10)
    if choice == 'punch':
        return random.randint(player.attack + 4, player.attack + 9)
    return None

#my asian roots
def samurai_attack(choice, player):
    if choice == 'throwing knife':
        return random.randint(player.attack + 4, player.attack + 9)
    if choice == 'katana slash':
        return random.randint(player.attack + 6, player.attack +12)
    if choice == 'hilt strike':
        return random.randint(player.attack + 3, player.attack + 8)
    return None

#similar to viking 
def hercules_attack(choice, player):
    if choice == 'stone throw':
        return random.randint(player.attack + 6, player.attack + 13)
    if choice == 'club strike':
        return random.randint(player.attack + 8, player.attack +15)
    if choice == 'power punch':
        return random.randint(player.attack + 5, player.attack + 12)
    return None

characters = {
    "archer": Fighter(
        "Archer", 100, 12, 3, 20, 15, #values are: HP, attack, defense, dodge(in percentage), crit(%)
        {"arrow shot": archer_attack,
        "bow strike": archer_attack,
        "knee strike": archer_attack},
        "side dodge" #defense technique
    ),
    "viking": Fighter(
        "Viking", 130, 15, 5, 10, 10, #HP, attack, dodge, crit
        {"axe throw": viking_attack,
        "overhead axe swing": viking_attack,
        "shoulder bash": viking_attack},
        "shield block"
    ),
    "illusionist": Fighter(
        "Illusionist", 90, 14, 2, 25, 20,
        {"illusionary projectile": illusionist_attack,
        "ethereal blade": illusionist_attack,
        "mind shock": illusionist_attack},
        "mirror illusion"
    ),
    "king": Fighter(
        "King", 110, 13, 4, 15, 15,
        {"royal decree": king_attack,
        "sword strike": king_attack,
        "punch": king_attack},
        "raise knight's shield"
    ),
    "samurai": Fighter(
        "Samurai", 105, 14, 3, 20, 20,
        {"throwing knife": samurai_attack,
        "katana slash": samurai_attack,
        "hilt strike": samurai_attack},
        "katana parry"
    ),
    "hercules": Fighter(
        "Hercules", 140, 16, 6, 5, 10,
        {"stone throw": hercules_attack,
        "club strike": hercules_attack,
        "power punch": hercules_attack},
        "forearm block"
    )
}
#quotes for more drama, i used gpt for this part for creative in this warrior style
quotes_intro = {
    "archer": [
        "“My arrows never miss… unless I want them to.”",
        "“Stay still. It only hurts the first time.”"
    ],
    "viking": [
        "“I was born in battle… and I’ll die in one.”",
        "“Your skull will make a fine trophy.”"
    ],
    "illusionist": [
        "“Reality is fragile… allow me to break it for you.”",
        "“Do you see me? Or just what I allow you to see?”"
    ],
    "king": [
        "“Kneel before your rightful ruler.”",
        "“A true king fears nothing—not even death.”"
    ],
    "samurai": [
        "“My blade follows the path of honor.”",
        "“One strike. One truth.”"
    ],
    "hercules": [
        "“Strength decides fate — and I have plenty.”",
        "“Let the earth tremble beneath my power!”"
    ]
}

quotes_victory = {
    "archer": "“Swift, silent, and deadly. Another target falls.”",
    "viking": "“Victory! I will drink to this tonight!”",
    "illusionist": "“Did you really think you were fighting alone?”",
    "king": "“The realm is safe under my rule once more.”",
    "samurai": "“Victory through discipline. Honor above all.”",
    "hercules": "“None can withstand the strength of a demigod!”"
}

quotes_defeat = {
    "archer": "“I… missed?”",
    "viking": "“Bah… a warrior’s death… at last…”",
    "illusionist": "“You broke the illusion… impressive…”",
    "king": "“A king… never truly falls…”",
    "samurai": "“My blade… was too slow…”",
    "hercules": "“Even the mighty… can be defeated…”"
}

#heres the main part
print("Choose your character:")
time.sleep(1.5)
for key in characters:
    print(f"- {key}") #key is characters
    time.sleep(1)
while True:
    choice = input("Your choice: ")
    if choice in characters:
       break
    print('Character not found, try again.')
time.sleep(1.5)

player = characters[choice]
print(f"\n{player.name} says: {random.choice(quotes_intro[choice])}")
time.sleep(2)

#here we choose our enemy
print('\nChoose your enemy:')
time.sleep(1)
for key in characters:
    print (f'- {key}')
    time.sleep(1)
while True:
    enemy_choice = input('Enemy choice: ')
    if enemy_choice in characters:
        break
    print('enemy not found, type better')
enemy = characters[enemy_choice]
time.sleep(1.5)
print(f"\n{enemy.name} growls: {random.choice(quotes_intro[enemy_choice])}")
time.sleep(2)

#we can see our characters
print(f"\nYou chose: {player.name}")
print(f"Your enemy: {enemy.name}")
time.sleep(1.5)

print('\nTHE FIGHT BEGINS!!!')
time.sleep(1)

block_mode = False #this is for the block move to turn off

#main battle
while player.is_alive() and enemy.is_alive():
    print(f'\nYour HP: {player.hp} , Enemy HP: {enemy.hp}') #just out hp
    time.sleep(1)

    print("\nAvailable attacks:") #a list of attacks we can use for the character
    time.sleep(1)
    for attack in player.abilities:
        print(f"- {attack}")
    print("- block (defense)")
    time.sleep(1)
    command = input("enter command: ")
    time.sleep(1)
    if command in player.abilities:
        dmg = player.abilities[command](command, player)

    elif command == 'block':
        block_mode = True #we block an attack from enemy
        print (f'You are using defense: {player.defense_name}')
        dmg = None #if player is not attacking
    else:
        print('Unknown command!')
        continue

    if dmg is not None: #if player attacks
        dealt = enemy.take_damage(dmg)
        print(f'You dealt {dealt} damage!')
    time.sleep(1.5)

#enemy attack
    if enemy.is_alive():
        enemy_move = random.choice(list(enemy.abilities.keys()))
        enemy_dmg = enemy.abilities[enemy_move](enemy_move, enemy)#attack and victim basically
        print(f"\nEnemy uses: {enemy_move}")

    #if we use block move
        if block_mode:
            enemy_dmg //= 2 #when we do block and enemy attacks us, damage will be less cause we have a block
            block_mode = False
            print("Your block reduced the damage!")

        taken = player.take_damage(enemy_dmg)
        print(f"You take {taken} damage!")
        time.sleep(1.5)

#heres game over
if player.is_alive():
    print('\nWin! You defeated the enemy!')
    time.sleep(1)
    print(f"{player.name} says: {quotes_victory[choice]}")
    time.sleep(1)
    print(f"{enemy.name} whispers: {quotes_defeat[enemy_choice]}")
else:
    print('\nYou lost! Game over.')
    time.sleep(1)
    print(f"{enemy.name} says: {quotes_victory[enemy_choice]}")
    time.sleep(1)
    print(f"{player.name} whispers: {quotes_defeat[choice]}")