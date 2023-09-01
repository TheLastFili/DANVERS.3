import logging
logging.basicConfig(level=logging.INFO)
import random
import time
import variables as var
from colorama import Fore, Back
import TheySeeMeRolling as roll
import CharacterFunctions as char
import GameFunctions as gam

# Greeting
print(
    Back.BLACK + Fore.LIGHTCYAN_EX + "Welcome to D.A.N.V.E.R.S! I am your Duel Assessment aNd Violent Encounter Research Simulator. "
                                     "\nYou may call me Dany. ")

# Setting everything up
att_bonus = 0
att_crits_made = 0

def_bonus = 0
def_crits_made = 0

player_stats = var.IronManStats
opp_stats = var.IronManStats
character_stat_list = [var.DummyStats, var.IronManStats, var.CaptainAmericaStats, var.RedSkullStats]
character_attack_list = [var.DummyAttStat, var.IronManAttStat, var.CaptainAmericaAttStat, var.RedSkullAttStat]
character_power_list = [var.DummyPowers, var.IronManPowers, var.CaptainAmericaPowers, var.RedSkullPowers]
dist_list = [[0,0,25], [1,26, 76], [2, 77, 152], [3, 153, 203], [4, 204, 254], [5, 255, 276], [6, 278, 999]]

# MAIN LOOP
while True:
    # Removing Dazed and setting Health to Injured Health
    if var.continued == 1:
        if var.player_dazed == 1 and var.opp_actions_used == 2:
            var.player_injured = 1
            var.player_dazed = 0
            var.player_health = player_stats[int(2)]
        if var.opp_dazed == 1 and var.pl_actions_used == 2:
            var.opp_injured = 1
            var.opp_dazed = 0
            var.opp_health = opp_stats[int(2)]

    if var.continued == 0:
        var.player_energy = 0
        var.opp_energy = 0
        var.opp_dazed = 0
        var.player_dazed = 0
        var.player_health = 0
        var.opp_health = 0
        var.player_KO = 0
        var.opp_KO = 0
        var.turn = 0

        # Lists and selections
        character_list = ["Dummy", "Iron Man", "Captain America", "Red Skull"]
        leadership_list = ["None", "A Day Unlike Any Other", "Master of Evil"]

        # Get player stats
        print(Fore.LIGHTGREEN_EX + f"Choose your character:")
        for i, item in enumerate(character_list):
            print(f"{i}. {item}")
        var.curr_player_nr = int(input())
        player_stats = character_stat_list[int(var.curr_player_nr)]
        var.player_power_list = character_power_list[int(var.curr_player_nr)]
        var.curr_player = player_stats[0]
        var.player_health = player_stats[1]
        var.curr_move = player_stats[3]
        if var.curr_player_nr + 1 > len(character_list):
            print("Invalid input. Try again.")
            continue

        print(f"Choose you leadership: ")
        for i, item in enumerate(leadership_list):
            print(f"{i}. {item}")
        var.pl_leadership_nr = int(input())
        var.pl_leadership = leadership_list[int(var.pl_leadership_nr)]
        if var.pl_leadership_nr + 1 > len(leadership_list):
            print("Invalid input. Try again.")
            continue
        if var.pl_leadership == "A Day Unlike Any Other" and var.pl_has_used_superpower == 0:
            var.pl_energy_modifier = 1

        # Get opponent stats
        print(Fore.LIGHTRED_EX + f"Choose your opponent: ")
        for i, item in enumerate(character_list):
            print(f"{i}. {item}")
        var.curr_opp_nr = int(input())
        opp_stats = character_stat_list[int(var.curr_opp_nr)]
        var.curr_opp = opp_stats[0]
        var.opp_health = opp_stats[1]

        if var.curr_opp_nr + 1 > len(character_list):
            print("Invalid input. Try again.")
            continue

        # Fight back? Priority?
        var.opp_fights = input("Would you like them to fight back? Y/N \n")
        if var.opp_fights.upper() == "Y":
            var.opp_active = 1
            var.priority_nr = int(input(f"Who has priority? 0 {var.curr_player} (Player) 1 {var.curr_opp} (AI)"))
            if var.priority_nr == 1:
                var.who_is_attacking = "Opponent"
        elif var.opp_fights.upper() == "N":
            var.opp_active = 0

    # POWER PHASE
    if var.opp_dazed == 1:
        if var.pl_actions_used < 2:
            var.who_is_attacking = "Player"
            var.opp_actions_used = 2
    # Next turn
    if var.turn == 0:
        gam.new_turn()

    if var.opp_active == 0:
        if var.pl_actions_used == 2:
            gam.new_turn()

    if var.opp_active == 1 and var.opp_dazed == 0 and var.opp_actions_used == 2 and var.priority_nr == 1:
        var.who_is_attacking = "Player"

    if var.opp_active == 1 and var.opp_dazed == 0 and var.opp_actions_used == 2 and var.priority_nr == 0:
        gam.new_turn()

    if var.who_is_attacking == "Player" and var.priority_nr == 1 and var.pl_actions_used == 2:
        gam.new_turn()

    # Calculate the distance, I am on my way... ## This could probably be simpler, but I'm not sure how yet
    for e in dist_list:
        if e [1] <= var.distance_mm <= e[2]:
            var.range_category = e[0]
            print (var.range_category)

    # Give me data
    print(Fore.LIGHTCYAN_EX + f"\nTurn  {var.turn}")
    print(f"Player: {var.curr_player} (Player), {var.player_health} Health, {var.player_energy} Energy")
    if var.opp_dazed == 0:
        print(f"Opponent: {var.curr_opp} (AI), {var.opp_health} Health, {var.opp_energy} Energy\n")
    elif var.opp_dazed == 1:
        print(Back.BLACK + Fore.LIGHTCYAN_EX + f"{var.curr_opp} (AI) is dazed!\n")

    if var.player_dazed == 0 and var.who_is_attacking == "Player":
        print(f"Actions available: {2 - var.pl_actions_used}, Distance is {var.range_category},"
              f" {var.curr_player} can move {var.curr_move}")
        if var.curr_move == "S":
            var.curr_move_mm = 86
            print(Fore.LIGHTYELLOW_EX + f"{var.pl_base_space}" + "." * int(86 / 5))
        if var.curr_move == "M":
            print(Fore.LIGHTYELLOW_EX + f"{var.pl_base_space}" + "." * int(127 / 5))
            var.curr_move_mm = 127
        if var.curr_move == "L":
            print(Fore.LIGHTYELLOW_EX + f"{var.pl_base_space}" + "." * int(184 / 5))
            var.curr_move_mm = 184
        print(Fore.LIGHTGREEN_EX + f"{var.pl_base_size}" + Fore.LIGHTCYAN_EX + "-" * int((var.distance_mm / 5))
              + Fore.LIGHTRED_EX + f"{var.opp_base_size}")
        print(f"{var.pl_base_space}" + " " * int((25 / 5)) + "1" + " " * int((47 / 5)) + "2" + " " * int((76 / 5)) + "3"
              + " " * int((51 / 5)) + "4" + " " * int((51 / 5)) + "5")
        # Player choice
        var.pl_can_use_superpower = 0
        for p in var.player_power_list:
            if p[2] <= var.player_energy + var.pl_energy_modifier and p[3] == "A" and p[5] == 0:
                var.pl_can_use_superpower = 1

        if var.pl_can_use_superpower == 1:
            var.pl_action = int(
                input(Fore.LIGHTCYAN_EX + "Would you like to (0) move, (1) attack or (2) use a superpower?\n"))
        else:
            var.pl_action = int(input(Fore.LIGHTCYAN_EX + "Would you like to (0) move or (1) attack?\n"))

    elif var.player_dazed == 1:
        print(f"No actions available, Player is dazed.")

    # Player choice: Move
    if int(var.pl_action) == 0:
        char.move()
        var.pl_actions_used += 1
        var.continued = 1
        continue

    # PLayer choice: Superpower
    if int(var.pl_action) == 2:
        for p in var.player_power_list:
            if p[2] <= var.player_energy + var.pl_energy_modifier and p[3] == "A" and p[5] == 0:
                print(str(p[0]) + " " + str(p[1]))
                var.curr_power_nr = int(input())

        if var.curr_player == "Red Skull":
            if var.curr_power_nr == 0:
                char.power_cube()

            if var.curr_power_nr == 1:
                char.move()
        var.continued = 1
        continue

    # Player choice: Attack
    # IRON MAN POWERS
    if var.pl_leadership == "A Day Unlike Any Other" and var.pl_has_used_superpower == 1:
        var.pl_energy_modifier = 0

    if var.curr_player == "Dummy":
        var.att_dice = (input("Choose your attack strength.\n"))
    if var.curr_player == "Iron Man" and var.who_is_attacking == "Player":
        if var.player_energy + var.pl_energy_modifier >= 2:
            Friday = (input("Do you want to use your FRIDAY AI? Y/N \n"))
            if Friday.upper() == "Y":
                att_bonus += 2
                var.player_energy -= (2 - var.pl_energy_modifier)
                var.pl_has_used_superpower = 1

    # CAPTAIN AMERICA ATTACKS AND POWERS
    ### BODYGUARD DOESN'T DO ANYTHING IN CURRENT ITERATION
    if var.curr_player == "Captain America" and var.who_is_attacking == "Opponent" and var.player_energy + var.pl_energy_modifier >= 2:
        VibraniumShield = (input("Do you want to use your Vibranium Shield? Y/N \n"))
        if VibraniumShield.upper() == "Y":
            def_bonus += 2
            # if var.pl_leadership == "A Day Unlike Any Other" and var.pl_has_used_superpower == 0:
            #     var.player_energy -= 1
            #     print(f"A day unlike Any Other! (Cost reduced by 1)")
            # else:
            var.player_energy -= (2 - var.pl_energy_modifier)
            var.pl_has_used_superpower = 1
    # RED SKULL ATTACKS AND SKILLS

    # Player Attacks Block
    if var.who_is_attacking == "Player":
        var.attack_finder = character_attack_list[int(var.curr_player_nr)]
        for e in var.attack_finder:
            if e[4] <= var.player_energy and e[2] >= var.range_category:
                print(str(e[0]) + " " + str(e[1]))
                var.available_list.append(e[1])

        if not var.available_list:
            print(f"No attacks available. Insufficient energy or out of range.")
            var.continued = 1
            continue

        if var.curr_attack_nr > len(character_attack_list):
            print("Invalid input. Try again.")
            var.continued = 1
            continue
        var.curr_attack_nr = int(input())

        var.curr_attack = var.attack_finder[int(var.curr_attack_nr)]
        var.att_type = var.curr_attack[5]
        var.att_dice = var.curr_attack[3] + int(att_bonus)
        var.player_energy -= var.curr_attack[4]
        var.defense_look_up = character_stat_list[int(var.curr_opp_nr)]
        var.def_dice = var.defense_look_up[int(var.att_type + 6)] + int(def_bonus)

    # AI ATTACKS! ###This needs to be completely revamped
    # Player is targeted, reactive superpowers
    var.pl_can_use_superpower = 0
    for p in var.player_power_list:
        if p[2] <= var.player_energy and p[3] == "R" and p[5] == 0:
            var.pl_can_use_superpower = 1
            var.curr_power_nr = int(input(f"Do you want to (1) continue or (2) use {p[1]}?"))
    if var.curr_player == "Red Skull" and var.curr_power_nr == 2:
        print("Hail Hydra! Protect me, my minions! [Effect not yet implemented.]")
        var.player_energy -= var.player_power_list[2][2]
        ###At some point, there will be cannon fodder nearby.
    if var.curr_opp == "Dummy" and var.who_is_attacking == "Opponent":
        var.att_type = 0
        var.att_dice = 2 + int(att_bonus)
        var.attack_is_gainer = 1

    if var.curr_opp == "Iron Man" and var.who_is_attacking == "Opponent":
        var.curr_attack_nr = 0
        var.curr_attack = var.IronManAttStat[int(var.curr_attack_nr)]
        if var.opp_energy >= 4:
            att_bonus += 2
            var.opp_energy -= 2
        var.att_type = var.curr_attack[5]
        var.att_dice = var.curr_attack[3] + int(att_bonus)

    if var.curr_opp == "Captain America" and var.who_is_attacking == "Player" and var.opp_energy >= 4:
        def_bonus += 2
        var.opp_energy -= 2
    if var.curr_opp == "Captain America" and var.who_is_attacking == "Opponent" and var.range_category >= 3:
        var.curr_attack_nr = 0
        var.curr_attack = var.IronManAttStat[int(var.curr_attack_nr)]
        var.att_type = var.curr_attack[5]
        var.att_dice = var.curr_attack[3] + int(att_bonus)
        var.opp_energy += 1

    if var.curr_opp == "Red Skull" and var.who_is_attacking == "Opponent":
        var.att_type = 1
        var.att_dice = 5 + int(att_bonus)
        var.attack_is_gainer = 1

    if var.who_is_attacking == "Opponent":
        var.defense_look_up = character_stat_list[int(var.curr_player_nr)]
        var.def_dice = var.defense_look_up[int(var.att_type + 6)] + int(def_bonus)
    ###NEED TO REWORK AI ENDS HERE
    print(Fore.LIGHTRED_EX + "Attacking with strength " + str(var.att_dice) + ".\n")
    if var.who_is_attacking == "Player":
        var.pl_actions_used += 1
    if var.who_is_attacking == "Opponent":
        var.opp_actions_used += 1
    print(Fore.LIGHTGREEN_EX + "Defending with strength " + str(var.def_dice) + ".\n")

    # ATTACK ROLLS
    while True:
        if roll.att_rolled < int(var.att_dice):
            roll.roll_adie()
        else:
            break

    gam.print_att_results()

    # ROLL DEFENDER DICE

    while True:
        if roll.def_rolled < int(var.def_dice):
            roll.roll_ddie()
        else:
            break

    gam.print_def_results()

    # CRIT RESOLVE ATTACK

    if roll.att_cr_added < int(roll.att_cr_ct1):
        att_crits_made = 1
        print(Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + "ATTACK CRITS!\n")
        time.sleep(1)

    while True:
        if roll.att_cr_added < int(roll.att_cr_ct1):
            roll.roll_cradie()
        else:
            break

    if att_crits_made == 1:
        gam.print_att_results()
    att_successes = roll.att_hi_ct + roll.att_wi_ct + roll.att_cr_ct1 + roll.att_cr_ct2

    if roll.def_cr_added < int(roll.def_cr_ct1):
        def_crits_made = 1
        print(Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + "DEFENSE CRITS!\n")
        time.sleep(1)

    while True:
        if roll.def_cr_added < int(roll.def_cr_ct1):
            roll.roll_crddie()
        else:
            break

    if def_crits_made == 1:
        gam.print_def_results()

    if var.who_is_attacking == "Player" and var.curr_opp == "Captain America" and var.opp_injured == 1:
        def_successes = roll.def_sh_ct + roll.def_wi_ct + roll.def_cr_ct1 + roll.def_cr_ct2 + roll.def_bl_ct
        print("I can do this all day!")
    elif var.who_is_attacking == "Opponent" and var.curr_player == "Captain America" and var.player_injured == 1:
        def_successes = roll.def_sh_ct + roll.def_wi_ct + roll.def_cr_ct1 + roll.def_cr_ct2 + roll.def_bl_ct
        print("I can do this all day!")
    else:
        def_successes = roll.def_sh_ct + roll.def_wi_ct + roll.def_cr_ct1 + roll.def_cr_ct2
    print(Back.RED + Fore.LIGHTWHITE_EX + "Total attack successes: " + str(att_successes) + "\n")
    print(Back.GREEN + Fore.LIGHTWHITE_EX + "Total defense successes: " + str(def_successes) + "\n")
    time.sleep(1)

    if var.curr_attack[8] == 1 and roll.att_wi_ct > 0 and var.who_is_attacking == "Player":  # Pushes that require wilds
        char.push()
                                                                                            # Pushes that just work

    ###THROWS NEED TERRAIN
    if var.curr_attack[10] == 1 and var.who_is_attacking == "Player":  # Throws that just work
        char.throw()

    if var.curr_player == "Red Skull" and var.curr_attack_nr == 1 and roll.att_wi_ct > 0 and var.who_is_attacking == "Player":
        print(Back.BLACK + Fore.LIGHTMAGENTA_EX + f"SAPPING POWER!")
        if roll.att_wi_ct > var.opp_energy:
            var.player_energy += var.opp_energy
            var.opp_energy = 0
        else:
            var.opp_energy -= roll.att_wi_ct
            var.player_energy += roll.att_wi_ct

    if var.curr_attack[8] == 0 and roll.att_wi_ct > 0 and var.who_is_attacking == "Opponent":
        print(Back.BLACK + Fore.LIGHTMAGENTA_EX + "COULD PUSH DEFENDER S.")

    var.net_damage = att_successes - def_successes
    if var.net_damage < 0:
        var.net_damage = 0
    if var.opp_dazed == 1 and var.who_is_attacking == "Player":
        var.net_damage = 0
    if var.player_dazed == 1 and var.who_is_attacking == "Opponent":
        var.net_damage = 0

    if opp_stats[10] == 1 and var.net_damage > 1 and var.who_is_attacking == "Player": 
        var.net_damage -= 1
        if var.curr_player == "Iron Man":
            print(Back.BLACK + Fore.LIGHTMAGENTA_EX + "I am the Invincible Iron Man! Damage reduced by 1.")

    if player_stats[10] == 1 and var.net_damage > 1 and var.who_is_attacking == "Opponent":
        var.net_damage -= 1
        if var.curr_player == "Iron Man":
            print(Back.BLACK + Fore.LIGHTMAGENTA_EX + "I am the Invincible Iron Man! Damage reduced by 1.")
        
    if var.who_is_attacking == "Player":
        gam.deal_dmg_to_opp()

    if var.who_is_attacking == "Opponent":
        if var.net_damage <= var.player_health:
            var.player_health -= var.net_damage
        else:
            var.net_damage = var.player_health
            var.player_health -= var.net_damage
        print(Back.BLACK + Fore.LIGHTRED_EX + "DAMAGE INFLICTED: " + str(var.net_damage) + "\n")
        var.player_energy += var.net_damage
        
        if var.net_damage > 0:
            print(Back.BLACK + Fore.LIGHTGREEN_EX + f"{var.curr_player} (Player) gained {var.net_damage} energy.")
        if var.player_energy > 10:
            var.player_energy = 10
        if var.curr_attack[6] == 1:
            var.opp_energy += var.net_damage
            if var.net_damage > 0:
                print(Back.BLACK + Fore.LIGHTRED_EX + f"{var.curr_opp} (AI) gained {var.net_damage} energy.")
        if var.curr_attack[7] == 1:
            var.opp_energy += 1
            print(Back.BLACK + Fore.LIGHTRED_EX + f"{var.curr_player} (AI) gained 1 energy.")
        if var.opp_energy > 10:
            var.opp_energy = 10

    if var.player_health > 0:
        print(
            Back.BLACK + Fore.LIGHTCYAN_EX + f"{var.curr_player} (Player), Health: {var.player_health}, Energy: {var.player_energy}")
    else:
        if var.player_dazed == 0:
            print(Back.BLACK + Fore.LIGHTCYAN_EX + f"{var.curr_player} (Player) was dazed!\n")
            var.player_dazed = 1
        elif var.player_dazed == 1:
            print(Back.BLACK + Fore.LIGHTCYAN_EX + f"{var.curr_player} (Player) was KO'd!\n")
            var.player_dazed = 0
            var.player_KO = 1
            print(Back.BLACK + Fore.LIGHTCYAN_EX + "Game over, you were KO'd.")
            break

    if var.opp_health > 0:
        print(
            Back.BLACK + Fore.LIGHTCYAN_EX + f"{var.curr_opp} (AI) Health: {var.opp_health}, Energy: {var.opp_energy}")
    else:
        if var.opp_dazed == 0:
            print(Back.BLACK + Fore.LIGHTCYAN_EX + f"{var.curr_opp} (AI) was dazed!\n")
            var.opp_dazed = 1
        elif var.opp_dazed == 1:
            print(Back.BLACK + Fore.LIGHTCYAN_EX + f"{var.curr_opp} (AI) is dazed!\n")
        elif var.opp_injured == 1:
            print(Back.BLACK + Fore.LIGHTCYAN_EX + f"{var.curr_opp} (AI) was KO'd!\n")
            var.opp_injured = 0
            var.opp_KO = 1
            break
            
    ### RICOCHET RULE!
    # AFTER DAMAGE IS DEALT
    if var.curr_player == "Captain America" and var.curr_attack_nr == 1 and roll.att_wi_ct >= 1:
        print("RICOCHET!")
        roll.reset_dice()
        while True:
            if att_rolled < int(var.att_dice):
                roll.roll_adie()
            else:
                gam.print_att_results()

    if var.curr_attack[10] == 1 and var.net_damage >= 1:
        char.throw()

    if var.curr_player == "Red Skull" and var.curr_attack_nr == 2 and roll.att_wi_ct > 0 and var.who_is_attacking == "Player":
        print(Back.BLACK + Fore.LIGHTMAGENTA_EX + "REALITY WARP! Enemies within 1 stunned!")
        ### RED SKULLS UNLEASH THE CUBE GOES HERE ONCE CONDITIONS ARE IMPLEMENTED, So do after combat skill
    
    if var.pl_leadership == "Master of Evil" and var.net_damage > 0:
        var.player_energy += 1

    # RESET DICE ROLLS
    roll.reset_dice()
    att_bonus = 0
    att_rolled = 0
    att_crits_made = 0

    def_bonus = 0
    def_rolled = 0
    def_crits_made = 0

    var.pl_can_use_superpower = 0
    var.available_list.clear()

    for p in var.player_power_list:
        if p[2] <= var.player_energy and p[3] == "A" and p[5] == 0:
            var.pl_can_use_superpower = 1

    if var.pl_can_use_superpower == 1:
        var.pl_action = int(
            input(Fore.LIGHTCYAN_EX + "Would you like to (1) continue or (2) use a superpower?\n"))

    if int(var.pl_action) == 2:
        for p in var.player_power_list:
            if p[2] <= var.player_energy and p[3] == "A" and p[5] == 0:
                print(str(p[0]) + " " + str(p[1]))
                var.curr_power_nr = int(input())

        if var.curr_player == "Red Skull":
            if var.curr_power_nr == 0:
                print("Behold the Power of the Cosmic Cube! 3 Energy gained")
                var.player_energy += 3
                roll.roll_cudie()
                print(f"The Cube damages you for {roll.cube_pain}.")
                var.player_health -= roll.cube_pain
                print(f"{roll.cube_pass} dice fall in your favour.\n")
                var.player_power_list[0][5] = 1

            if var.curr_power_nr == 1:
                var.moving_direction = int(input("Do you want to move (0) forward or (1) back?"))
                var.moving = int(input(f"How much of Range 2 do you want to move? (1) 25% (2) 50% (3) 75% (4) 100%"))
                if var.moving_direction == 0:
                    var.final_move_mm = int(var.moving * 0.25 * 76)
                    var.distance_mm -= var.final_move_mm
                if var.moving_direction == 1:
                    var.distance_mm += var.final_move_mm
                var.player_energy -= (3 - var.pl_energy_modifier)

    check = input(Back.BLACK + Fore.LIGHTCYAN_EX +
                  "Do you want to continue, start again or quit? Press any key to continue, R to restart or Q to end: ")
    if check.upper() == "R":  # go back to the top
        var.continued = 0
        continue

    if check.upper() == "Q":
        print("Session terminates")
        break

    else:
        if var.opp_KO == 0:
            var.continued = 1
        if var.opp_KO == 1:
            var.continued = 0
        if var.opp_active == 1 and var.pl_actions_used == 2:
            if var.who_is_attacking == "Player":
                var.who_is_attacking = "Opponent"
        if var.opp_active == 1 and var.opp_actions_used == 2:
            if var.who_is_attacking == "Opponent":
                var.who_is_attacking = "Player"
        continue
