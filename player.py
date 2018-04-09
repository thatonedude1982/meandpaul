class Player(object):

    def __init__(self, playerName, playerNumber):
        self.name = playerName
        self.number = playerNumber
        self.dead = False
        self.turnsUntilDead = 50
        self.Cholera = False
        self.Typhoid = False
        self.Measles = False
        self.inventory = list()
        self.supplies = list()
        self.nextTurn = 0
        pass

    def setName(self, playerName):
        self.name = playerName

    def getName(self):
        return self.name

    def setCholera(self):
        self.Cholera = True

    def setTyphoid(self):
        self.Typhoid = True

    def setMeasles(self):
        self.Measles = True
    
    def setHeal(self):
        if self.Measles == True:
            self.Measles = False
        elif self.Cholera == True:
            self.Cholera = False
        elif self.Typhoid == True:
            self.Typhoid = False

    def killPlayer(self, currentPlayer):
        currentPlayer.dead = False
        
    #build methods for keeping track of which cards are in the players hand
    def playerHand(self, currentPlayer):
        #call deckmanager for the player
        print("test")
