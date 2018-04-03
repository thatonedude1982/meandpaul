#module for keeping track of the decks of cards that have been turned in or have yet to be picked up
import itertools, random
from player import Player as pl

i = 0 # establishing global var to iterate through shuffled deck. 
# need to find a way to store this number so each card is not drawn
# from the top of the deck. Also, need to figure out how to treat
# each card as unique.
supplyDeck = list(itertools.product(range(26)))
list2 = list(itertools.product(range(26)))
inventory = list()
#shuffle
'''
def randomize():   # shuffles the supply deck
    random.shuffle(supplyDeck)
'''
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

list2[0] = "100 Bullets"
list2[1] = "100 Bullets"
list2[2] = "Clothes"
list2[3] = "Clothes"
list2[4] = "Clothes"
list2[5] = "Oxen"
list2[6] = "Oxen"
list2[7] = "Oxen"
list2[8] = "Clean Water"
list2[9] = "Clean Water"
list2[10] = "Clean Water"
list2[11] = "Clean Water"
list2[12] = "Clean Water"
list2[13] = "200 Lbs of Food"
list2[14] = "200 Lbs of Food"
list2[15] = "200 Lbs of Food"
list2[16] = "Spare Parts"
list2[17] = "Spare Parts"
list2[18] = "Spare Parts"
list2[19] = "Spare Parts"
list2[20] = "Medicine"
list2[21] = "Medicine"
list2[22] = "Medicine"
list2[23] = "Medicine"
list2[24] = "Medicine"
list2[25] = "Medicine"

def initDraw(pl):
   print("You got: ")
   while len(inventory) < 5:
       rando = random.randint(0,26)
       if supplyDeck[rando] == list2[rando]:
           inventory.append([supplyDeck[rando]])
           del(supplyDeck[rando])
       else:
           return
       print(inventory)
''' Loop needs to be iterated through all four players
        so that all players get a full hand of supply cards.
        That code will go here. At this point, we need to start 
        merging the other pieces of code so we can run it from
        "the top"
'''
def draw(pl):
    print("You got: ")
    print(supplyDeck[random.randrange(0,25)])

def discard():
    print ("test")    

def buy():
    print("test")

#randomize() # this print is just in to test shuffle function
#print (supplyDeck)

initDraw(pl) # this is for first draw of game where players get 5 cards

draw(pl)# this is for any subsequent draws made by players.
