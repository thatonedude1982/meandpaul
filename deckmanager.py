#module for keeping track of the decks of cards that have been turned in or have yet to be picked up
import itertools, random
from player import Player as pl

globcounter = 0
supplyDeck = list(itertools.product(range(26)))
inventory = list(itertools.product(range(8)))

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

#shuffle
def randomize():   
    random.shuffle(supplyDeck)
    
def initDraw(pl): #this handles the initial supply deck each player receives.
    print("You got: ")
    global globcounter
    for i in range (0,4):
        while globcounter < 25: #handles iterating through entire deck while making it "end of deck aware"
            pl.inventory = (supplyDeck[globcounter])
            globcounter += 1
            print pl.inventory
            #inventory.append(supplyDeck[globcounter])
            #code to iterate loop to next player
            break
    else: # if out of cards, reshuffle and start at the top.
        randomize()
        globcounter = 0
      
def draw(pl):
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

def discard():#eventually writing a discard function 
    print ("test")    

def buy():#eventually a function to trade two of the same cards for one supply of players choice
    print("test")

randomize() #calling shuffle function for testing

initDraw(pl) # this is for first draw of game where players get 5 cards calling for testing
print (pl.inventory) # printing pl.inventory to ensure player inventory is being updated.

draw(pl)# this is for any subsequent draws made by players calling for testing
