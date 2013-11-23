from triple_draw_poker.controller.AmountToCallController import getAmountToCall

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def initHand(GameDetails, HandDetails, bankroll, players, bet_level):
    for i in range(0, players):
        GameDetails.players.append(Player(bankroll))
