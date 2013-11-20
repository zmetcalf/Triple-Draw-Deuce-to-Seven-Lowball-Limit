# Game details contains items that last longer than one hand.
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

    def getBetLevel(self):
        return self.bet_level

    def getNumberOfPlayers(self):
        return self.number_of_players

    def initDealer(self):
        x = random.randint(0, len(self.players) - 1)
        self.players[x].setDealer()

    def setPlayerViewStatus(self, player_position):
        self.players[player_position].setPlayerViewStatus()

    def getPlayerViewStatus(self, player_position):
        return self.players[player_position].getPlayerViewStatus()

    def getPlayers(self):
        return self.players
