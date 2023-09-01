#This is for things the characters do aside from rolling and for power
import TheySeeMeRolling as roll
import variables as var
from colorama import Fore, Back

### COMMON

def move():
    var.moving_direction = int(input("Do you want to move (0) forward or (1) back?"))
    var.moving = int(input(f"How much of {var.curr_move} do you want to move? (1) 25% (2) 50% (3) 75% (4) 100%"))
    var.final_move_mm = int(var.moving * 0.25 * var.curr_move_mm)
    if var.moving_direction == 0:
        var.distance_mm -= var.final_move_mm
    if var.moving_direction == 1:
        var.distance_mm += var.final_move_mm

def push():
    if var.curr_player == "Iron Man" or var.curr_player == "Red Skull":
        print(Back.BLACK + Fore.LIGHTMAGENTA_EX + f"PUSH DEFENDER {var.curr_attack[9]}?")
        if var.curr_attack[9] == "S":
            var.pushthrow_mm = 86
        var.pushing = int(input(f"Push {var.curr_attack[9]}, up to {var.pushthrow_mm}mm."))
        var.distance_mm += var.pushing

    if var.curr_player == "Captain America":
        if var.opp_size <= int(3):
            print(Back.BLACK + Fore.LIGHTMAGENTA_EX + f"PUSH DEFENDER {var.curr_attack[9]}?")
            if var.curr_attack[9] == "S":
                var.pushthrow_mm = 86
        var.pushing = int(input(f"Push {var.curr_attack[9]}, up to {var.pushthrow_mm}mm."))
        var.distance_mm += var.pushing

def throw():
    if var.curr_player == "Captain America":
        if var.opp_size <= int(3):
            print(Back.BLACK + Fore.LIGHTMAGENTA_EX + f"THROW DEFENDER {var.curr_attack[11]}?")
            if var.curr_attack[11] == "S":
                var.pushthrow_mm = 86
            var.throwing = int(input(f"Throw {var.curr_attack[9]}, up to {var.pushthrow_mm}mm."))
            var.distance_mm += var.throwing

    if var.curr_player == "Red Skull":
        if var.opp_size <= int(3):
            print(Back.BLACK + Fore.LIGHTMAGENTA_EX + f"THROW DEFENDER {var.curr_attack[11]}?")
            if var.curr_attack[11] == "S":
                var.pushthrow_mm = 86
            var.throwing = int(input(f"Throw {var.curr_attack[9]}, up to {var.pushthrow_mm}mm."))
            var.distance_mm += var.throwing

### SPECIFIC

def power_cube():
    print("Behold the Power of the Cosmic Cube! 3 Energy gained")
    var.player_energy += 3
    roll.roll_cudie()
    print(f"The Cube damages you for {roll.cube_pain}.")
    var.player_health -= roll.cube_pain
    print(f"{roll.cube_pass} dice fall in your favour.")
    var.player_power_list[0][5] = 1
