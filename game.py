import random

while True:
    player_name = input("What is your name, traveler? ")
    player_health = 100
    
    def monster_dice_roll():
        monster_dice = random.randint(1, 6)
        if monster_dice == 1:
            monster_type = "witch"
        elif monster_dice == 2:
            monster_type = "syclix"
        elif monster_dice == 3:
            monster_type = "midusa"
        elif monster_dice == 4:
            monster_type = "minitar"
        elif monster_dice == 5:
            monster_type = "cyeribis"
        elif monster_dice == 6:
            monster_type = "zombie"
        return monster_type
    
    def Chosse_spices():
        player_spices = input("What is your species type? (a) troll, (b) org, (c) vampire, (d) human: ")
        if player_spices.lower() == 'a':
            print("You have chosen to be a troll, you are strong but slow.")
            attacks = ["club smash", "ground pound", "troll roar"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "troll"
        elif player_spices.lower() == 'b':
            print("You have chosen to be an org, you are fierce and powerful but not very smart.")
            attacks = ["smash", "roar", "charge"]
            dmg1, dmg2, dmg3 = 5, 10, 15
            spices = "org"
        elif player_spices.lower() == 'c':
            print("You have chosen to be a vampire, you are fast and durable but are hackable.")
            attacks = ["shriek", "bite", "cyber attack"]
            dmg1, dmg2, dmg3 = 15, 5, 10
            spices = "vampire"
        elif player_spices.lower() == 'd':
            print("You have chosen to be a human, you are balanced and versatile but not durable.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "human"
        else:
            print("Invalid choice! spices has been set to human by default.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "human"
        
        # Return all 5 values as a tuple
        return (spices, attacks, dmg1, dmg2, dmg3)

    choice = input(f"Welcome {player_name}, you have been chosen to be the hero of this world. Do you accept? (y/n) ")
    
    if choice.lower() == 'y':
        # FIX: We must "unpack" the 5 things the function returns into 5 variables
        player_spices, current_attacks, attack1_dmg, attack2_dmg, attack3_dmg = Chosse_spices()

        print(f"Great! {player_name} the {player_spices}, your adventure begins now.")
        
        input("""How this game will work: when you defeat a monster you gain skill points...
              (Press Enter to continue)""")
        
        choice = input("Are you ready to start your adventure? (y/n) ")
        if choice.lower() == 'y':
            print("Let's begin!")
            
            # Start the game loop here
            while True:
                monster = monster_dice_roll()
                print(f"\nA wild {monster} appeared!")
                print(f"Your health: {player_health}")
                print(f"Your attacks: {current_attacks}")
                
                # Simple placeholder for combat
                action = input(f"Do you want to (f)ight or (r)un? ")
                if action.lower() == 'f':
                    print(f"You used {current_attacks[0]} and dealt damage!")
                    break # Breaking to prevent infinite loop for now
                else:
                    print("You ran away!")
                    break

    elif choice.lower() == 'n':
        print("Perhaps another time.")
        break
    else:
        print("Please enter 'y' or 'n'.")
