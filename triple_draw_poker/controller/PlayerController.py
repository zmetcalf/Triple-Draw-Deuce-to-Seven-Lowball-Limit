import random

from triple_draw_poker.model.HandDetails import HandDetails

def getActivePlayer(players):
    for player in players:
        if player.getActiveStatus():
            return player
    return False

def initDealer(players):
    x = random.randint(0, len(players) - 1)
    players[x].setDealer()
    players[x].setActive()

def checkIfDealerSet(players):
    for player in players:
        if player.getDealerStatus():
            return True
    return False

def advanceDealer(players):
    pointer = dealer_index = players.index(getDealer(players))
    players[dealer_index].setNonDealer()

    while pointer < len(players) - 1:
        pointer += 1
        if not players[pointer].getSittingOut():
            players[pointer].setDealer()
            players[pointer].setActive()
            return

    pointer = 0

    while pointer < dealer_index:
        if not players[pointer].getSittingOut():
            players[pointer].setDealer()
            players[pointer].setActive()
            return
        pointer += 1

def getDealer(players):
    for player in players:
        if player.getDealerStatus():
            return player
    return False

def playerBet(HandDetails, players, amount, raises):
    HandDetails.getPot().addBet(amount)
    return getActivePlayer(players).bet(amount, raises)

def setInactiveAllPlayers(players):
    for player in players:
        player.setInactive()

def setRaiser(players):
    for player in players:
        if player.getActiveStatus():
            player.setRaiser()
        else:
            player.setNonRaiser()

def changeActivePlayer(players):
    pointer = active_index =  players.index(getActivePlayer(players))
    players[pointer].setInactive()
    while pointer < len(players) - 1:
        pointer += 1
        if players[pointer].getInHand():
            players[pointer].setActive()
            return

    pointer = 0

    while pointer < active_index:
        if players[pointer].getInHand():
            players[pointer].setActive()
            return
        pointer += 1

def getPlayersInHand(players):
    active_players = 0
    for player in players:
        if player.getInHand():
            active_players += 1
    return active_players
