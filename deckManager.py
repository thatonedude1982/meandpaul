#module for keeping track of the decks of cards that have been turned in or have yet to be picked up

import itertools, random
import supplies

from player import Player as pl

#globcounter = 0

inventory = list(itertools.product(range(8)))



#shuffle
def randomize(list):   
    random.shuffle(list)
    
#commented until function can be made universal
'''
def initDraw(): #this handles the initial supply deck each player receives.
    print("You got: ")
    global globcounter
    for i in range (0,4):
        while globcounter < 25: #handles iterating through entire deck while making it "end of deck aware"
            pl.inventory = (supplyDeck[globcounter])
            globcounter += 1
            print (pl.inventory)
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
'''

def discard():#eventually writing a discard function 
    print ("test")    

def buy():#eventually a function to trade two of the same cards for one supply of players choice
    print("test")

def cardRoll(pl, cardType):     #takes a number to denote card type 
    roll = dice.roll()
    outcome = 1             #the condition of the card is true until it isnt
    if cardType == 1:       #card type is a wagon calamity
        if roll == 4 or roll == 5 or roll == 6:
            standardMessage = "The Wagon is repaired"
            outcome = 0
            #return card to the deck code
        else:
            #logic depending on card
            print("test else reached")
    elif cardType == 2 or cardType == 3:    #river trail cards
        if roll/2:
            standardMessage = "You have successfully forded the river"
            outcome = 0
        elif not roll/2:
            if cardType == 3 and roll == 1: #Player drowns
                pl.killPlayer(pl) 
            elif cardType == 2:
                #player loses 1 supply card
                print("card type 2 reached")
            elif cardType == 3:
                cardRoll(pl+1, 3)    #play passes to the left/next player to roll                
    return outcome, standardMessage


#randomize() #calling shuffle function for testing

#initDraw(pl) # this is for first draw of game where players get 5 cards calling for testing

#print(pl.inventory) # printing pl.inventory to ensure player inventory is being updated.

#draw(pl)# this is for any subsequent draws made by players calling for testing