from player import Player as pl
import Die as dice
import deckManager as dm

class CalamityCard(object):

#universal variables
    standardMessage = ''
    global calamityDeck
    calamityDeck = []

    

    def __init__(self):
        self.name = 'name'
        #self.image = ''

    #universal clear calamity function
    #def clearCalamity():
        #if town is played

        #elif specific supplies are played

    def buildCalamityDeck():
        i = 0
        while i < 32:
            if i < 2:
                calamityDeck.append("Bad Water")
            elif i < 4:
                calamityDeck.append("Inadequate Grass")
            elif i < 6:
                calamityDeck.append("Extreme Cold")
            elif i < 8:
                calamityDeck.append("Broken Tongue")
            elif i < 10:
                calamityDeck.append("Broken Axle")
            elif i < 12:
                calamityDeck.append("Broken Wheel")
            elif i < 14:
                calamityDeck.append("Dead Oxen")
            elif i < 16:
                calamityDeck.append("Cholera")
            elif i < 18:
                calamityDeck.append("Typhoid")
            elif i < 20:
                calamityDeck.append("Measles")
            elif i < 22:
                calamityDeck.append("Dysentery")
            elif i < 24:
                calamityDeck.append("Food")
            elif i < 26:
                calamityDeck.append("Starvation")
            elif i < 28:
                calamityDeck.append("Snake Bite")
            elif i < 30:
                calamityDeck.append("Thief")
            elif i < 32:
                calamityDeck.append("Broken Arm")
            i += 1
        dm.randomize(calamityDeck) 
        return calamityDeck


###Environmental calamity cards
    def badWater(self, playerName):
        self.name = 'Bad Water'
        #self.image = '/Resources/badWater.jpg'
        standardMessage = """Fulsh away bad water with 1 Clean Water Card. If 2 Bad Water 
        Cards are collected then two Oxen die. One round of play without an Oxen Card and 
        everyone in your party has DIED."""
        

    def inadequateGrass(self, playername):
        self.name = 'Inadequate Grass'
        #self.image = '/Resources/inadequateGrass.jpg'
        standardMessage = """If 2 Inadequate Grass Cards are face up then 2 Oxen die.
        One round of play without an Oxen Card and everyone in your party has died"""
        


    def extremeCold(self, playerName):
        self.name = 'Extreme Cold'
        #self.image = '/Resources/extremeCold.jpg'
        standardMessage = """Bundle up and beat the cold with 1 Clothing Card. One round of 
        play without a Clothing Card and you have DIED of extreme cold."""
###########################################################################################


###Vehicle calamity cards
    def brokenTongue(self, playerName):
        self.name = 'Broken Tongue'
        #self.image = '/Resources/brokenTongue.jpg'
        #call die roll based off user input like a mouse click
        msg = """1 Spare Parts Card must be used to repair the broken tongue. 
        One round of play without repair and everyone in your party has DIED."""
        if cardRoll(msg) == 1:
            pl.turnsUntilDeath = 1

    def brokenAxle(self, playerName):
        self.name = 'Broken Axle'
        #self.image = '/Resources/brokenAxle.jpg'
        #call die roll based off user input like a mouse click
        msg = """1 Spare Parts Card must be used to repair the broken axle. 
        One round of play without repair and everyone in your party has DIED."""
        if cardRoll(msg) == 1:
            pl.turnsUntilDeath = 1
            

    def brokenWheel(self, playerName):
        self.name = 'Broken Wheel'
        #self.image = '/Resources/brokenWheel.jpg'
        #call die roll based off user input like a mouse click
        msg = """1 Spare Parts Card must be used to repair the broken wheel. 
        One round of play without repair and everyone in your party has DIED."""
        if cardRoll(msg) == 1:
            pl.turnsUntilDeath = 1


    def deadOxen(self, playerName):
        self.name = 'Dead Oxen'
        #self.image = '/Resources/deadOxen.jpg'
        standardMessage = """2 Oxen have DIED. Play 1 Oxen Card to continue. One round of 
        play without an Oxen Card and everyone in your party has DIED."""

    ### moving this function to deckManager
    '''
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
        elif cardType == 2 or cardType == 3:    #cards are river trail cards
            if roll/2:
                standardMessage = "You have successfully forded the river"
                outcome = 0
            elif not roll/2:
                if cardType == 3 and roll == 1:
                    pl.dead == True
                elif cardType == 2:
                    #player loses 1 supply card
                elif cardType == 3:
                    #play passes to the left
                    
        return outcome, standardMessage
    '''

###########################################################################################
    

###Sickness calamity cards
    def cholera(self, playerName):
        self.name = 'Cholera'
        #self.image = '/Resources/cholera.jpg'
        standardMessage = """2 Medicine Cards can cure you. If any player draws another 
        Cholera Card before you're cured, you have Dien of cholera."""

    def typhoid(self, playerName):
        self.name = 'Typhoid'
        #self.image = '/Resources/typhoid.jpg'
        standardMessage = """1 Clean Water Card AND 1 Medicine Card can cure you. One round 
        of play without a cure and you have DIED of typhoid."""

    def measles(self, playerName):
        self.name = 'Measles'
        #self.image = '/Resources/measles.jpg'
        standardMessage = """Lose 1 turn, unless you or a trailmate plays 1 Medicine Card. 
        If another Measles Card is drawn before you are cured, you have DIED of measles."""

    def dysentery(self, playerName):
        self.name = 'Dysentery'
        #self.image = '/Resources/dysentery.jpg'
        standardMessage = "You have DIED of dysentery."
        pl.getName(playerName)
        pl.killPlayer()
###########################################################################################

###Miscellaneous calamity cards
    def food(self, playerName):
        self.name = 'Food'
        #self.image = '/Resources/food.jpg'
        standardMessage = """Collect 200 lbs of rabbit and bison if you have 1 Bullets 
        Card. Discard this card if you have no bullets."""
    
    def starvation(self, playerName):
        self.name = 'Starvation'
        #self.image = '/Resources/starvation.jpg'
        standardMessage = """Survive another day with 1 Food Card. Two rounds of play without 
        a Food Card and you have DIED of starvation."""

    def snakeBite(self, playerName):
        self.name = 'Snake Bite'
        #self.image = '/Resources/snakeBite.jpg'
        pl.killPlayer()

    def thief(self, playerName):
        self.name = 'Thief'
        #self.image = '/Resources/thief.jpg'
        #remove a supply card from the player

    def brokenArm(self, playernName):
        self.name = "Broken Arm"
        #self.image = '/Resources/brokenArm.jpg'
        pl.nextTurn = 2
###########################################################################################
    
    #buildCalamityDeck()
    #dm.randomize(calamityDeck)   
    #printed out for testing purposes

