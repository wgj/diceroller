#!/usr/bin/python

from random import choice

die = [1, 2, 3, 4, 5, 6]


def diceroll(dice):
    sum = 0
    for i in xrange(0, dice):
        sum += choice(die)
    return sum

rolls = 100

def simulation(rolls, dice):
    dice1_win = 0
    dice2_win = 0
    dice_tie = 0
    for i in xrange(1, rolls):
        dice1 = diceroll(1)
        dice2 = diceroll(1)
        if dice1 > dice2:
            dice1_win += 1
        if dice2 > dice1:
            dice2_win += 1
        if dice1 == dice2:
            dice_tie += 1
    return dice1_win, dice2_win, dice_tie
    

rolls = 100000

onedice_dice1_win, onedice_dice2_win, onedice_tie = simulation(rolls, 1)
twodice_dice1_win, twodice_dice2_win, twodice_tie = simulation(rolls, 2)


print 'Rolls:', rolls
print ''
print 'Each player rolls one die:'
tab = '    '
print tab + 'Player one wins: %.0f%%' % (100.0 * float(onedice_dice1_win) / float(rolls))
print tab + 'Player two wins: %.0f%%' % (100.0 * float(onedice_dice2_win) / float(rolls))
print tab + 'Draw: %.0f%%' % (100.0 * float(onedice_tie) / float(rolls))
print ''
print 'Each player rolls two dice:'
tab = '    '
print tab + 'Player 1 wins: %.0f%%' % (100.0 * float(twodice_dice1_win) / float(rolls))
print tab + 'Player 2 wins: %.0f%%' % (100.0 * float(twodice_dice2_win) / float(rolls))
print tab + 'Draw: %.0f%%' % (100.0 * float(twodice_tie) / float(rolls))
