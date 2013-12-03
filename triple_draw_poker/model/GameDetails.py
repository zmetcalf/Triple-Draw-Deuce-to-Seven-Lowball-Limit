# Game details contain items that last longer than one hand.
# This includes the players and initial settings

import random

from triple_draw_poker.model.Player import Player

class GameDetails:

    def __init__(self):
        self.number_of_players = 2
        self.bankroll = 1000
        self.players = []
        for i in range(0, self.number_of_players):
            self.players.append(Player(self.bankroll))
        self.initDealer()
        self.bet_level = 10

    def getActivePlayer(self):
        for player in self.players:
            if player.getActiveStatus():
                return player
        return False

    def getBetLevel(self):
        return self.bet_level

    def getNumberOfPlayers(self):
        return self.number_of_players

    def initDealer(self):
        x = random.randint(0, len(self.players) - 1)
        self.players[x].setDealer()

    def checkIfDealerSet(self):
        for player in self.players:
            if player.getDealerStatus():
                return True
        return False

    def advanceDealer(self):
        dealer_index = self.players.index(self.getDealer())
        if dealer_index == len(self.players) - 1:
            # TODO needs additional functionality to check if player is in hand
            self.players[0].setDealer()
        else:
            self.players[dealer_index + 1].setDealer()

        self.players[dealer_index].setNonDealer()

    def getDealer(self):
        for player in self.players:
            if player.getDealerStatus():
                return player
        return False

    def setPlayerViewStatus(self, player_position):
        self.players[player_position].setPlayerViewStatus()

    def getPlayerViewStatus(self, player_position):
        return self.players[player_position].getPlayerViewStatus()

    def getPlayers(self):
        return self.players

    def setActivePlayer(self, player_position):
        self.players[player_position].setActive()

    def setInactivePlayer(self, player_position):
        self.players[player_position].setInactive()

    def setInactiveAllPlayers(self):
        for player in self.players:
            player.setInactive()

    def playerBet(self, amount, raises):
        return self.getActivePlayer().bet(amount, raises)
