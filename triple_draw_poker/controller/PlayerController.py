import random

def getActivePlayer(players):
    for player in players:
        if player.getActiveStatus():
            return player
    return False

def initDealer(players):
    x = random.randint(0, len(players) - 1)
    players[x].setDealer()

def checkIfDealerSet(players):
    for player in players:
        if player.getDealerStatus():
            return True
    return False

def advanceDealer(players):
    dealer_index = players.index(getDealer(players))
    if dealer_index == len(players) - 1:
        # TODO needs additional functionality to check if player is in hand
        players[0].setDealer()
    else:
        players[dealer_index + 1].setDealer()

    players[dealer_index].setNonDealer()

def getDealer(players):
    for player in players:
        if player.getDealerStatus():
            return player
    return False

def playerBet(players, amount, raises):
    return getActivePlayer(players).bet(amount, raises)
