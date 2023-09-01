#Setting up game variable
continued = 0
priority_nr = 0
opp_fights = "N"
opp_active = 0
who_is_attacking = "Player"
distance_mm = 153  # Range 3, max distance 279
range_category = 5
move_category = "S"
final_move_mm = 0
pushing = 0
throwing = 0
moving = 0
moving_direction = 1
show_me_distance = distance_mm / 5
opp_action = 1
attack_finder = 0
defense_look_up = 0
pl_look_up = 0
opp_look_up = 0
pushthrow_mm = 0
turn = 0
net_damage = 0
#Setting up player variables
curr_player = "None"
curr_player_nr = 0
curr_move = "A"
curr_move_mm = 0
player_health = 0
player_energy = 0
player_dazed = 0
player_injured = 0
player_KO = 0
player_size = 0
pl_actions_used = 0
pl_action = 5
pl_leadership_nr = 0
pl_leadership = "None"
pl_has_used_superpower = 0
pl_base_size = "(...)"
pl_base_space = "     "
player_number = 0
curr_power_nr = 0
pl_can_use_superpower = 0
energy_mod = 0
player_power_list = None
pl_energy_modifier = 0
#Setting up opponent variables
curr_opp = "None"
curr_opp_nr = 0
opp_health = 0
opp_energy = 0
opp_dazed = 0
opp_injured = 0
opp_KO = 0
opp_size = 0
opp_actions_used = 0
opp_leadership_nr = 1
opp_leadership = "None"
opp_has_used_superpower = 0
opp_base_size = "(...)"
opp_number = 0

#Setting up attack roll variables
att_dice = 50
att_hi_ct = 0
att_cr_ct1 = 0
att_cr_ct2 = 0
att_wi_ct = 0
att_sh_ct = 0
att_fa_ct = 0
att_bl_ct = 0
att_bonus = 0
att_rolled = 0
att_crits_made = 0
att_cr_added = 0

#Setting up defense roll variables
def_dice = 30
def_hi_ct = 0
def_cr_ct1 = 0
def_cr_ct2 = 0
def_wi_ct = 0
def_sh_ct = 0
def_fa_ct = 0
def_bl_ct = 0
def_type = 0
def_bonus = 0
def_rolled = 0
def_crits_made = 0
def_cr_added = 0

#Setting up attack variables
att_type = 3
attack_is_gainer = 0
curr_attack = "None"
curr_attack_nr = -2

#Character Stat Library
character_list = ["Dummy", "Iron Man", "Captain America", "Red Skull"]
leadership_list = ["None", "A Day Unlike Any Other", "Master of Evil"]
available_list = []
# 0Name, 1HealthH, 2HealthI, 3MoveH, 4MoveI, 5Size, 6DPh, 7DEn, 8DMy, 9Base, 10RedDmgMin1
DummyStats = ["Dummy", 5, 5, "M", "M", 2, 3, 3, 3, "(...)", 0]
IronManStats = ["Iron Man", 5, 5, "M", "M", 2, 4, 3, 3, "(...)", 1]
CaptainAmericaStats = ["Captain America", 5, 6, "M", "M", 2, 4, 4, 3, "(...)", 0]
RedSkullStats = ["Red Skull", 6, 6, "M", "M", 2, 4, 3, 3, "(...)", 0]

#Character Attack Library
    #Attack Names
IronManAttNam = ["0 Repulsor Blast", "1 Homing Rockets", "2 UniBeam"]
CaptainAmericaAttNam = ["0 Strike", "1 Shield Throw", "2 Shield Slam"]
RedSkullAttNam = ["0 Strike", "1 Cosmic Blast", "2 Unleash the Cube"]

    #Attack Stats
# 0Nr, 1Name, 2Range, 3Strength, 4Cost, 5Type, 6IsGainer, 7Gain1, 8Push, 9PushDist,
# 10Throw, 11ThrowDist, 12Pierce
DummyAttStat = [[0, "Strike", 2, 5, 0, 0, 1, 0, 1, "S", 0, "X", 0],
                [1, "Laaaaser", 4, 3, 0, 1, 0, 1, 0, "X", 0, "X", 0]]

IronManAttStat = [[0, "Repulsor Blast", 4, 4, 0, 1, 1, 0, 1, "S", 0, "X", 0],
                  [1, "Homing Rockets", 5, 5, 2, 0, 0, 0, 0, "X", 0, "X", 0],
                  [2, "Unibeam", 5, 6, 4, 1, 0, 0, 0, "X", 0, "X", 0]]

CaptainAmericaAttStat = [[0, "Strike", 2, 5, 0, 0, 1, 0, 1, "S", 0, "X", 0],
                         [1, "Shield Throw", 4, 5, 0, 0, 0, 1, 0, "X", 0, "X", 0],  # Ricochet implemented?
                         [2, "Shield Slam", 2, 6, 2, 0, 0, 0, 0, "X", 1, "S", 0]]  # Implement throw

RedSkullAttStat = [[0, "Strike", 2, 5, 0, 0, 1, 0, 1, "S", 0, "X", 0],
                   [1, "Cosmic Blast", 4, 5, 1, 1, 0, 0, 0, "X", 0, "X", 0],  # Sap Power
                   [2, "Unleash the Cube", 4, 7, 4, 1, 0, 0, 0, "X", 0, "X", 0]]  # Implement Throw, Reality Warp

#Character powers
#0: Nr, 1Name, 2Cost, 3Type Active/Reactive 4OncePerTurn 5HasBeenUsed
DummyPowers = []
IronManPowers = []
CaptainAmericaPowers = []
RedSkullPowers = [[0, "Cosmic Cube", 0, "A", 1, 0],
                   [1, "Master of the Cube", 3, "A", 1, 0],  ###Actually for DANVERS yes, but not for other chars
                   [2, "Hail Hydra", 2, "R", 1, 0]]

