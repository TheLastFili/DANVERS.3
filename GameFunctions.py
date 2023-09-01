#This is for shared functions
import variables as var
from colorama import Fore, Back
import TheySeeMeRolling as roll
import time
def new_turn():
    var.player_energy += 1
    var.opp_energy += 1
    var.turn += 1
    var.pl_actions_used = 0
    var.opp_actions_used = 0
    var.pl_has_used_superpower = 0
    for p in var.player_power_list:
        p[5] = 0

def print_att_results():
    print(Back.RED + Fore.LIGHTWHITE_EX + "ATTACK ROLL")  ##Print result functions
    print(Back.BLACK + Fore.LIGHTWHITE_EX + str(roll.att_hi_ct) + " Hit")
    print(Fore.LIGHTCYAN_EX + str(roll.att_wi_ct) + " Wild")
    print(Fore.LIGHTYELLOW_EX + str(roll.att_cr_ct1 + roll.att_cr_ct2) + " Crit")
    print(Fore.LIGHTBLACK_EX + str(roll.att_sh_ct) + " Shield")
    print(Fore.LIGHTBLACK_EX + str(roll.att_fa_ct) + " Failure")
    print(Fore.LIGHTBLACK_EX + str(roll.att_bl_ct) + " Blank\n")
    time.sleep(1)

def print_def_results():
    print(Back.GREEN + Fore.LIGHTWHITE_EX + "DEFENSE ROLL")
    print(Back.BLACK + Fore.LIGHTBLACK_EX + str(roll.def_hi_ct) + " Hit")
    print(Fore.LIGHTCYAN_EX + str(roll.def_wi_ct) + " Wild")
    print(Fore.LIGHTYELLOW_EX + str(roll.def_cr_ct1 + roll.def_cr_ct2) + " Crit")
    print(Fore.LIGHTWHITE_EX + str(roll.def_sh_ct) + " Shield")
    print(Fore.LIGHTBLACK_EX + str(roll.def_fa_ct) + " Failure")
    print(Fore.LIGHTBLACK_EX + str(roll.def_bl_ct) + " Blank\n")
    time.sleep(1)

def deal_dmg_to_opp():
    if var.net_damage <= var.opp_health:
        var.opp_health -= var.net_damage
    else:
        var.net_damage = var.opp_health
        var.opp_health -= var.net_damage
    print(Back.BLACK + Fore.LIGHTRED_EX + "DAMAGE INFLICTED: " + str(var.net_damage) + "\n")
    var.opp_energy += var.net_damage

    if var.net_damage > 0:
        print(Back.BLACK + Fore.LIGHTGREEN_EX + f"{var.curr_opp} (AI) gained {var.net_damage} energy.")
    if var.opp_energy > 10:
        var.opp_energy = 10
    if var.curr_attack[6] == 1:
        var.player_energy += var.net_damage
        if var.net_damage > 0:
            print(Back.BLACK + Fore.LIGHTRED_EX + f"{var.curr_player} (Player) gained {var.net_damage} energy.")
    if var.curr_attack[7] == 1:
        var.player_energy += 1
        print(Back.BLACK + Fore.LIGHTRED_EX + f"{var.curr_player} (Player) gained 1 energy.")
    if var.player_energy > 10:
        var.player_energy = 10

def deal_dmg_to_pl():
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
