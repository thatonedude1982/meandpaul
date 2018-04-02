from player import Player as pl

class CalamityCard(object):
    
    def __init__(self):
        self.name = 'name'
        self.image = ''

    #def clearCalamity():
        #if town is played

        #elif specific supplies are played

    def brokenTongue(self):
        self.name = 'Broken Tongue'

    def snakeBite(self):
        pl.killPlayer()
        self.name = 'Snake Bite'

    #def thief():
        #remove a supply card from the player

    #def brokenArm():
        #player loses 2 turns

    def dysentery(self, playerName):
        self.name = 'Dysentery'
        pl.getName(playerName)
        pl.killPlayer()

