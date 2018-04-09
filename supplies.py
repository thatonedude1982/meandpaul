import itertools
import deckManager as dm
from player import Player as pl

supplyDeck = list(itertools.product(range(26)))
globcounter = 0

def createSupplyDeck():
    global supplyDeck

    #populating supply list
    supplyDeck[0] = "100 Bullets"
    supplyDeck[1] = "100 Bullets"
    supplyDeck[2] = "Clothes"
    supplyDeck[3] = "Clothes"
    supplyDeck[4] = "Clothes"
    supplyDeck[5] = "Oxen"
    supplyDeck[6] = "Oxen"
    supplyDeck[7] = "Oxen"
    supplyDeck[8] = "Clean Water"
    supplyDeck[9] = "Clean Water"
    supplyDeck[10] = "Clean Water"
    supplyDeck[11] = "Clean Water"
    supplyDeck[12] = "Clean Water"
    supplyDeck[13] = "200 Lbs of Food"
    supplyDeck[14] = "200 Lbs of Food"
    supplyDeck[15] = "200 Lbs of Food"
    supplyDeck[16] = "Spare Parts"
    supplyDeck[17] = "Spare Parts"
    supplyDeck[18] = "Spare Parts"
    supplyDeck[19] = "Spare Parts"
    supplyDeck[20] = "Medicine"
    supplyDeck[21] = "Medicine"
    supplyDeck[22] = "Medicine"
    supplyDeck[23] = "Medicine"
    supplyDeck[24] = "Medicine"
    supplyDeck[25] = "Medicine"

    dm.randomize(supplyDeck)

    #printed out for testing purposes
    #i = 0
    #for item in supplyDeck:
        #print(supplyDeck[i])
        #i+=1

def initDraw(): #this handles the initial supply deck each player receives.
    suppliesInventory = list()
    global globcounter
    for i in range (0,4):
        while globcounter < 25: #handles iterating through entire deck while making it "end of deck aware"
            suppliesInventory.append(supplyDeck[globcounter])
            globcounter += 1
            break
    else: # if out of cards, reshuffle and start at the top.
        dm.randomize(supplyDeck)
        globcounter = 0
    return suppliesInventory
      
def draw():
    global globcounter
    for i in range(1): #almost the same as the initDraw function, but one card at a time.
        while globcounter < 25:
            print("You got: ")
            inventory.append(supplyDeck[globcounter])
            print(supplyDeck[globcounter])
            globcounter += 1
            break
        else:
            randomize()
            globcounter = 0
