import random
import variables as var
#Dice value
cube_rolled = 0
cube_pain = 0
cube_pass = 0

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

# 0-1: hit, 2: crit, 3: wild, 4: shield, 5: failure, 6-7: blank
def roll_adie():
    dice = random.randrange(0, 7)
    global att_hi_ct
    global att_cr_ct1
    global att_wi_ct
    global att_fa_ct
    global att_sh_ct
    global att_bl_ct
    global att_rolled

    if dice == 0 or dice == 1:
        att_hi_ct = att_hi_ct + 1
    if dice == 2:
        att_cr_ct1 = att_cr_ct1 + 1
    if dice == 3:
        att_wi_ct = att_wi_ct + 1
    if dice == 4:
        att_sh_ct = att_sh_ct + 1
    if dice == 5:
        att_fa_ct = att_fa_ct + 1
    if dice == 6 or dice == 7:
        att_bl_ct = att_bl_ct + 1
    att_rolled = att_rolled + 1

    # while True:
    #     if att_rolled < int(var.att_dice):
    #         roll_adie()
    #     else:
    #         break

def roll_ddie():
    dice = random.randrange(0, 7)
    global def_hi_ct
    global def_cr_ct1
    global def_wi_ct
    global def_fa_ct
    global def_sh_ct
    global def_bl_ct
    global def_rolled

    if dice == 0 or dice == 1:
        def_hi_ct = def_hi_ct + 1
    if dice == 2:
        def_cr_ct1 = def_cr_ct1 + 1
    if dice == 3:
        def_wi_ct = def_wi_ct + 1
    if dice == 4:
        def_sh_ct = def_sh_ct + 1
    if dice == 5:
        def_fa_ct = def_fa_ct + 1
    if dice == 6 or dice == 7:
        def_bl_ct = def_bl_ct + 1
    def_rolled = def_rolled + 1

def roll_cradie():
    dice = random.randrange(0, 7)
    global att_hi_ct
    global att_cr_ct1
    global att_wi_ct
    global att_fa_ct
    global att_sh_ct
    global att_bl_ct
    global att_rolled
    global att_cr_added
    global att_cr_ct2

    if dice == 0 or dice == 1:
        att_hi_ct = att_hi_ct + 1
    if dice == 2:
        att_cr_ct2 = att_cr_ct2 + 1
    if dice == 3:
        att_wi_ct = att_wi_ct + 1
    if dice == 4:
        att_sh_ct = att_sh_ct + 1
    if dice == 5:
        att_fa_ct = att_fa_ct + 1
    if dice == 6 or dice == 7:
        att_bl_ct = att_bl_ct + 1
    att_cr_added = att_cr_added + 1

def roll_crddie():
    dice = random.randrange(0, 7)
    global def_hi_ct
    global def_cr_ct1
    global def_wi_ct
    global def_fa_ct
    global def_sh_ct
    global def_bl_ct
    global def_rolled
    global def_cr_added
    global def_cr_ct2

    if dice == 0 or dice == 1:
        def_hi_ct = def_hi_ct + 1
    if dice == 2:
        def_cr_ct2 = def_cr_ct2 + 1
    if dice == 3:
        def_wi_ct = def_wi_ct + 1
    if dice == 4:
        def_sh_ct = def_sh_ct + 1
    if dice == 5:
        def_fa_ct = def_fa_ct + 1
    if dice == 6 or dice == 7:
        def_bl_ct = def_bl_ct + 1
    def_cr_added = def_cr_added + 1

def roll_cudie():
    dice = random.randrange(0, 7)
    global cube_pain
    global cube_pass
    global cube_rolled

    if dice == 5:
        cube_pain += 1
    else:
        cube_pass += 1
    cube_rolled = cube_rolled + 1

    while True:
        if cube_rolled < 5:
            roll_cudie()
        else:
            break


def reset_dice():
    global att_hi_ct
    global att_cr_ct1
    global att_cr_ct2
    global att_wi_ct
    global att_fa_ct
    global att_sh_ct
    global att_bl_ct
    global att_rolled
    global att_cr_added
    global att_dice

    global def_hi_ct
    global def_cr_ct1
    global def_cr_ct2
    global def_wi_ct
    global def_fa_ct
    global def_sh_ct
    global def_bl_ct
    global def_rolled
    global def_cr_added
    global def_dice

    att_hi_ct = 0
    att_cr_ct1 = 0
    att_cr_ct2 = 0
    att_wi_ct = 0
    att_sh_ct = 0
    att_fa_ct = 0
    att_bl_ct = 0

    att_dice = 0
    att_rolled = 0
    att_cr_added = 0

    def_hi_ct = 0
    def_cr_ct1 = 0
    def_cr_ct2 = 0
    def_wi_ct = 0
    def_sh_ct = 0
    def_fa_ct = 0
    def_bl_ct = 0

    def_dice = 0
    def_rolled = 0
    def_cr_added = 0
