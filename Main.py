import Die as dice
import supplies as supply
import menu as menu
import deckManager as deck
import trail
import os
import deckManager as deck
from calamity import CalamityCard as cal
from player import Player as pl
 


players = {}


"""
Begin Game
    Build decks
    Number of players (2 - 6) [Networking capability?]
    Initial hand draw - Trails, Supplies
Play Game
    Player 1 - trail card
    if calamity, draw calamity - player affects
    if ford, roll dice
    
    Player 2 - trail or supply card

Win or Lose Game

"""


def gameStart():
    #Building and shuffling decks
    trail.trailDeckBuild()
    supply.createSupplyDeck()
    cal.buildCalamityDeck()
    

    #menu call
    if(menu.initialMenu()) == 1:
        buildPlayers()  

    menu.playerTurnMenu(players[0])

def buildPlayers():
        numberPlayers = input("How many travelers are making the journey? ")
        
        global players

        i = 1
        while i <= int(numberPlayers):
            name = input("Enter player {}'s name: ".format(i))
            players[i-1] = pl(name, i)
            i+=1


        for item in players:
            print("Player {}, {}, drew these trail cards:".format(players[item].number, players[item].name))
            players[item].inventory = trail.initTrailDraw()
            print(players[item].inventory)
            print("And these supplies:")
            players[item].supplies = supply.initDraw()
            print(players[item].supplies)
            os.system("pause")


gameStart()