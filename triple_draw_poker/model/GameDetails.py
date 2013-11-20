import random

from triple_draw_poker.model.Players import Players

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
        x = random.randint(0, self.player - 1)
        self.players[x].setDealer()
