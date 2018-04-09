#create a reusable menu system to be called in the main game 
###test purposes###
import Die
###################

def initialMenu():
    str1 = "Local Play - L"
    str2 = "Network Play - N"
    print("Welcome to the Dysentery Trail")
    print("Please select from the following:")
    playVar = input('{}\n{}\n'.format(str1, str2))

    if playVar.upper() == 'L':
        print("You have chosen wisely")
        #call code to build the number of players using a return to main
        return 1
    elif playVar.upper() == 'N':
        print("You have chosen poorly")
        #call code for network setup and connection - not built
        return 0
    else:
        print("Please enter a valid menu selection")
        if(initialMenu()==1):
            return 1

def playerTurnMenu(player):
    #give player option to show hand or play cards
    #show player the choice to play either a supply or trail card
    #do auto draw of trail card if trail is played

    #code for test purposes#
    '''drawnCard = ""
    drawnCard = trail.trailDraw()
    players[0].trailHand.append(drawnCard)
    print (players[0].trailHand)
    print ("Yes")
    drawnCard = trail.trailDraw()
    players[1].trailHand.append(drawnCard)
    print (players[1].trailHand)'''
    
    trailHand = ["Ford River", "Ford River", "Trail Calamity", "Blank Trail"]
    supplyHand = ["Bullets", "Clean Water", "Clothes"]

    ########################

    #begin turn
    print (player)
    print ("The current calamities are: ")
    print ("What action would you like to perform?")
    
    while True:
        opt0 = "Display Hand - D"
        opt1 = "Play Trail card - T"
        opt2 = "Play Supply card - S"
        action = input("{}\n{}\n{}\n".format(opt0, opt1, opt2))

        if action.upper() == "D":
            showHand(trailHand, supplyHand)
    #player action
        if action.upper() == "T":
            handSize = len(trailHand)
            #print("Which card would you like to play?")
        #print(player.trailHand)
            for i in range(handSize):
                print ("{}. {}".format(i, trailHand[i]))

            card = int(input("Which card to you want to play? \n"))

            playTrail(trailHand[card], supplyHand)
            #call function for card action
            #call function/ insert code to remove card from list

        if action.upper() == "S":
            handSize = len(supplyHand)
            print("Which card would you like to play?")
        #print(player.trailHand)
            for i in range(handSize):
                print ("{}. {}".format(i, supplyHand[i]))

        else:
            print("That is not a valid option. Please choose again.")

    #end turn
    


def showHand(trails, supplies):
    print ("Hand")
    trailSize = len(trails)
    supplySize = len(supplies)

    print("TRAILS - ")
    for i in range(trailSize):
        print ("{}. {}".format(i, trails[i]))

    print("SUPPLIES - ")
    for i in range(supplySize):
        print ("{}. {}".format(i, supplies[i]))
    #pull up player's dealt cards

def playTrail(card, hand): #import player instead of supply hand
    if card == "Blank Trail":
        print("You've traveled without any issues.")

    if card == "Ford River":
        print ("You must roll a dice to ford the river successfully. \n Rolling dice.")
        number = Die.roll()
        print (number)
        if (number % 2 == 0):
            print ("You have forded the river successfully!")
        else:
            print("You have failed to ford the river. Please choose one supply to lose:")
            amount = len(hand)
            for i in range(amount):
                print("{}. {}".format(i, hand[i]))
            dropSupply = int(input())
            print ("You are losing {}".format(hand[dropSupply]))
    
    if card == "Trail Calamity":
        

    
#def networkSetup():
    #choose server or client

playerTurnMenu("Shawn")