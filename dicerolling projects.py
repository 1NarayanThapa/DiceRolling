# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 06:58:33 2020

@author: acer
"""

import random
def main():
        player1 = 0
        player1wins=0
        player2 = 0
        player2wins=0
        rounds = 1
        while rounds  !=4:
            print("round"+str(rounds))
            player1= dice_roll()
            player2= dice_roll()
            print("player1 roll" + str (player1))
            print("player2 roll" + str (player2))
            if player1==player2:
                
                print("DRAW\n")
            elif player1>player2:
                player1wins=player1wins+1
                print("player1 wins!!!!!:\n")

            else:
                 player2wins=player2wins+1
                 print("player 2 is wins!!!!:\n")

                
           # print(player1)
            rounds = rounds + 1
            if player1wins==player2wins:
                print("DRAW GAME")
            elif player1wins>player2wins:
                print("player1 is finally winner!!! round won: "+str(player1wins))
                
            else:
                print("player 2 is finnally winner!!!round won:"+str(player2wins))
def dice_roll():
    diceRoll=random.randint(1,6)
    return diceRoll
main()
