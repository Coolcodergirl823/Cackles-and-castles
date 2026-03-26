import random
from CAC import cheatcode   # cheatcode is a STRING

def the_second_game():

    def Choose_species():
        player_health = 100
        player_species = input("What is your species type? (a) troll, (b) orc, (c) vampire, (d) human: ")

        if player_species.lower() == 'a':
            print("You have chosen to be a troll, you are strong but slow.")
            attacks = ["club smash", "ground pound", "troll roar"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "troll"

        elif player_species.lower() == 'b':
            print("You have chosen to be an orc, you are fierce and powerful but not very smart.")
            attacks = ["smash", "roar", "charge"]
            dmg1, dmg2, dmg3 = 5, 10, 15
            species = "orc"

        elif player_species.lower() == 'c':
            print("You have chosen to be a vampire, you are fast and durable but are vulnerable to sunlight.")
            attacks = ["shriek", "bite", "blood drain"]
            dmg1, dmg2, dmg3 = 15, 5, 10
            species = "vampire"

        elif player_species.lower() == 'd':
            print("You have chosen to be a human, you are balanced and versatile but not durable.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "human"

        else:
            print("Invalid choice! species has been set to human by default.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "human"

        return (species, attacks, dmg1, dmg2, dmg3)

    def new_monster_generator():
        dice = random.randint(1,18)

        monster_type = "unknown"
        monster_health = random.randint(10,50)
        monster_attack = "hit"
        monster_attack_dmg = 5

        if dice == 1:
            monster_type = "skellaten"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "arrow_shot"
                monster_attack_dmg = 5
            else:
                monster_attack = "call for backup"
                monster_attack_dmg = 0

        elif dice == 2:
            monster_type = "mummy"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "drain life"
                monster_attack_dmg = 10

        elif dice == 3:
            monster_type = "werewolf"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "claw swipe"
                monster_attack_dmg = 5
            else:
                monster_attack = "howl"
                monster_attack_dmg = 0

        elif dice == 4:
            monster_type = "gargoyal"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "stone throw"
                monster_attack_dmg = 5
            else:
                monster_attack = "petrify"
                monster_attack_dmg = 10

        elif dice == 5:
            monster_type = "Huldra"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "charm"
                monster_attack_dmg = 0
            else:
                monster_attack = "claw swipe"
                monster_attack_dmg = 5

        elif dice == 6:
            monster_type = "Liche"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "dark magic"
                monster_attack_dmg = 10
            else:
                monster_attack = "drain life"
                monster_attack_dmg = 5

        elif dice == 7:
            monster_type = "Gremlins"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "sabotage"
                monster_attack_dmg = 0
            else:
                monster_attack = "bite"
                monster_attack_dmg = 5

        elif dice == 8:
            monster_type = "Wraiths"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "drain life"
                monster_attack_dmg = 10
            else:
                monster_attack = "hit"
                monster_attack_dmg = 5

        elif dice == 9:
            monster_type = "Ghoul"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        elif dice == 10:
            monster_type = "Revenants"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        elif dice == 11:
            monster_type = "Cyclops"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        elif dice == 12:
            monster_type = "Yeti"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        elif dice == 13:
            monster_type = "witch"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "potion"
                monster_attack_dmg = 15
            else:
                monster_attack = "heal"
                monster_attack_dmg = 0

        elif dice == 14:
            monster_type = "goblin"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "kick"
                monster_attack_dmg = 5
            else:
                monster_attack = "stab"
                monster_attack_dmg = 10

        elif dice == 15:
            monster_type = "medusa"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "paralyze"
                monster_attack_dmg = 10

        elif dice == 16:
            monster_type = "minotaur"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "horse kick"
                monster_attack_dmg = 5
            else:
                monster_attack = "charge"
                monster_attack_dmg = 10

        elif dice == 17:
            monster_type = "cerberus"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "triple bite"
                monster_attack_dmg = random.randint(1,15)
            else:
                monster_attack = "bite"
                monster_attack_dmg = 10

        elif dice == 18:
            monster_type = "zombie"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        return monster_type, monster_health, monster_attack, monster_attack_dmg

    choice = input("welcom back travler our world is in distress agein and you will be the one to save it do you accept this quest (y/n) ")

    if choice.lower() == "y":
        player_health = 100
        fight_count = 0

        species, attacks, dmg1, dmg2, dmg3 = Choose_species()

        while player_health > 0:

            fight_count += 1

            # --- BOSS SETUP (every 5 fights) ---
            boss_name = None
            boss_health = 0
            boss_dmg = 0

            if fight_count % 30 == 0:
                boss_name = "FINAL BOSS – Shadow King"
                boss_health = 300
                boss_dmg = 18
                print(f"{boss_name} appears with {boss_health} HP!")
            elif fight_count % 25 == 0:
                boss_name = "Mythical Beast"
                boss_health = 250
                boss_dmg = 20
                print(f"{boss_name} appears with {boss_health} HP!")
                if player_health < 100:
                    player_health = 100
                player_health += 50
            elif fight_count % 20 == 0:
                boss_name = "Legendary Titan"
                boss_health = 200
                boss_dmg = 16
                print(f"{boss_name} appears with {boss_health} HP!")
                if player_health < 100:
                    player_health = 100
                player_health += 50
            elif fight_count % 15 == 0:
                boss_name = "Mega Golem"
                boss_health = 175
                boss_dmg = 14
                print(f"{boss_name} appears with {boss_health} HP!")
                if player_health < 100:
                    player_health = 100
                player_health += 50
            elif fight_count % 10 == 0:
                boss_name = "Stronger Demon"
                boss_health = 150
                boss_dmg = 12
                print(f"{boss_name} appears with {boss_health} HP!")
                if player_health < 100:
                    player_health = 100
                player_health += 50                

            elif fight_count % 5 == 0:
                boss_name = "Mini Boss"
                boss_health = 120
                boss_dmg = 10
                print(f"{boss_name} appears with {boss_health} HP!")
                if player_health < 100:
                    player_health = 100
                player_health += 50


            # --- BOSS FIGHT LOOP ---
            if boss_name is not None:
                while boss_health > 0 and player_health > 0:

                    attack_choice = input(f"Boss fight! Choose an attack from {attacks}: ")

                    # PLAYER ATTACKS
                    if attack_choice.lower() == attacks[0]:
                        boss_health -= dmg1
                        print(f"You used {attacks[0]} and dealt {dmg1} damage!")

                    elif attack_choice.lower() == attacks[1]:
                        boss_health -= dmg2
                        print(f"You used {attacks[1]} and dealt {dmg2} damage!")

                    elif attack_choice.lower() == attacks[2]:
                        boss_health -= dmg3
                        print(f"You used {attacks[2]} and dealt {dmg3} damage!")

                    elif attack_choice.lower() == cheatcode:
                        boss_health = 0
                        fight_count = 30
                        print("Cheat activated! Skipping to final boss!")
                        break

                    else:
                        print("Invalid attack! You miss your turn.")

                    if boss_health <= 0:
                        print(f"You defeated {boss_name}!")
                        if boss_name.startswith("FINAL BOSS"):
                            print("You saved the world! Game complete.")
                            return
                        break

                    print(f"{boss_name} attacks!")
                    player_health -= boss_dmg
                    print(f"It dealt {boss_dmg} damage! You now have {player_health} HP.")

                    if player_health <= 0:
                        print("You have been defeated by the boss...")
                        return

            else:
                # Normal monster encounter
                monster_type, monster_health, monster_attack, monster_attack_dmg = new_monster_generator()
                input(f"You have encountered a {monster_type} with {monster_health} HP!")

                while monster_health > 0 and player_health > 0:

                    attack_choice = input(f"What do you do? Choose an attack from {attacks}: ")

                    if attack_choice.lower() == attacks[0]:
                        monster_health -= dmg1
                        print(f"You used {attacks[0]} and dealt {dmg1} damage!")

                    elif attack_choice.lower() == attacks[1]:
                        monster_health -= dmg2
                        print(f"You used {attacks[1]} and dealt {dmg2} damage!")

                    elif attack_choice.lower() == attacks[2]:
                        monster_health -= dmg3
                        print(f"You used {attacks[2]} and dealt {dmg3} damage!")

                    elif attack_choice.lower() == cheatcode.lower():
                        monster_health = 0
                        fight_count = 29
                        print("Cheat activated! Jumping to final boss!")
                        break

                    else:
                        print("Invalid attack! You miss your turn.")

                    if monster_health <= 0:
                        print(f"You defeated the {monster_type}!")
                        break

                    print(f"The {monster_type} uses {monster_attack}!")
                    player_health -= monster_attack_dmg
                    print(f"It dealt {monster_attack_dmg} damage! You now have {player_health} HP.")

                    if player_health <= 0:
                        print("You have been defeated...")
                        return

    elif choice.lower() == "n":
        print("you are a coward!")