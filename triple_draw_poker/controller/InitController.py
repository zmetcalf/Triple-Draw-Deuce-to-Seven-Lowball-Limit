from triple_draw_poker.controller.AmountToCallController import getAmountToCall

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def initHand(GameDetails):
    hand_details = HandDetails()
    GameDetails.setInactiveAllPlayers()
    if GameDetails.checkIfDealerSet():
        GameDetails.initDealer()
    else:
        GameDetails.advanceDealer()
    return hand_details
