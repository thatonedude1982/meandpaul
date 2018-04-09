#module for the map cards
import itertools, random
from player import Player as pl
import deckManager as dm
import calamity as cal
globCounter1 = 0 #creating global counter to handle drawing cards and holding place in deck
trail = list(itertools.product(range(50))) #establishing trail length at 50 units
trailCards = list(itertools.product(range(56)))#establishing trail deck size at 56
trailInventory = list()#establishing player hand size at 6

#populating supply list in a more automated manner
def trailDeckBuild():
    #print ("Building...")
    for i in range(len(trailCards)):
        if i < 8:
            trailCards[i] = "Blank Trail"
            continue
        elif i < 10:
            trailCards[i] = "Fort"
            continue
        elif i < 12:
            trailCards[i] = "Town"
            continue
        elif i < 36:
            trailCards[i] = "Trail Calamity"
            continue
        elif i < 53:
            trailCards[i] = "Ford River"
            continue
        else:
            trailCards[i] = "Ford River--Danger"
            continue
        i += 1
    #shuffle
    dm.randomize(trailCards)


def initTrailDraw(): #Same function as initDraw for supply cards reworked for trail
    #print("You got: ")
    trailInventory = list()
    global globCounter1
    for i in range (0,5):
        while globCounter1 < 55: #handles iterating through entire deck while making it "end of deck aware"
            trailInventory.append(trailCards[globCounter1])
            #print(trailCards[globCounter1])
            globCounter1 += 1
            #code to iterate loop to next player
            break
        else: # if out of cards, reshuffle and start at the top.
            randomize()
            globCounter1 = 0
            print ("Out")
            trailInventory.append(trailCards[globCounter1])
            globCounter1 += 1
    
    return trailInventory

def trailDraw():
    global globCounter1
    drawnCard = ""
    print("You got: ")
    for i in range(1): #almost the same as the initDraw function, but one card at a time.
        while globCounter1 < 55:
            #trailInventory.append(trailCards[globCounter1])
            drawnCard = trailCards[globCounter1]
            print (drawnCard)
            #print(trailCards[globCounter1])
            globCounter1 += 1
            return drawnCard
            #break
        else:
            randomize()
            globCounter1 = 0
            #trailInventory.append(trailCards[globCounter1])
            drawnCard = trailCards[globCounter1]
            print (drawnCard)
            globCounter1 += 1
            return drawnCard
#trailDeckBuild()

#randomize()

#initTrailDraw()

#trailDraw()
