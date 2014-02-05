diceroller
==========
Simulate MTG player order rolls.

When playing "Magic: The Gathering" (https://en.wikipedia.org/wiki/Magic:_The_Gathering), players will often roll a dice to see who goes first.

This is well and good, however, some players will suggest using two dice for 'more random results', or 'less likely draws', and some will get down right indignant when you try to talk about the statistically likelihood of a fair dice roll.

I know a thing or two about stochastic systems, so I did up this short program to run simulations of dice rolls for one die, and two dice rolling.


Output
--------------
    wgjohnson$ ./diceroller.py 
    Rolls: 100000
    
    Each player rolls one die:
        Player one wins: 42%
        Player two wins: 41%
        Draw: 17%
    
    Each player rolls two dice:
        Player 1 wins: 42%
        Player 2 wins: 42%
        Draw: 17%

