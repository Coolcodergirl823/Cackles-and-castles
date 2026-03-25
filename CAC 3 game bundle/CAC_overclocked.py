import random

def new_monster_generator():
    dice = random.randint(1,12)
    if dice == 1:
        monster = "skellaten"
        

    if dice == 2:
        monster = "mummy"
    if dice == 3:
        monster = "werewolf"
    if dice == 4:
        monster = "gargoyal"
    if dice == 5:
        monster = "Huldra"
    if dice == 6:
        monster = "Liche"
    if dice == 7:
        monster = "Gremlins"
    if dice == 8:
        monster = "Wraiths"
    if dice == 9:
        monster = "Ghoul"
    if dice == 10:
        monster = "Revenants"
    if dice == 11:
        monster = "Cyclops"
    if dice == 12:
        monster = "Yeti"
def monster_dice_roll():
        monster_dice = random.randint(1, 6)
        if monster_dice == 1:
            monster_type = "witch"
            monster_health = 30
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "potion"
                monster_attack_dmg = 15
            elif attack_dice == 2:
                monster_attack = "heal" 
                monster_attack_dmg = 0
        elif monster_dice == 2:
            monster_type = "goblin"
            monster_health = 20
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "kick"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "stab" 
                monster_attack_dmg = 10
        elif monster_dice == 3:
            monster_type = "medusa"
            monster_health = 80
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "paralyze" 
                monster_attack_dmg = 10
        elif monster_dice == 4:
            monster_type = "minotaur"
            monster_health = 30
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "horse kick"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "charge" 
                monster_attack_dmg = 10
        elif monster_dice == 5:
            monster_type = "cerberus"
            monster_health = 40
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "triple bite"
                monster_attack_dmg = random.randint(1,15)
            elif attack_dice == 2:
                monster_attack = "bite" 
                monster_attack_dmg = 10
        elif monster_dice == 6:
            monster_type = "zombie"
            monster_health = 10
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        
        return (monster_type,monster_health,monster_attack,monster_attack_dmg)
