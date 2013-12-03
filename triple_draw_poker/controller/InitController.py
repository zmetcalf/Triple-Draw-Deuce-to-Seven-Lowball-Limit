from triple_draw_poker.controller.AmountToCallController import getAmountToCall
from triple_draw_poker.controller.PlayerController import checkIfDealerSet, \
      initDealer, advanceDealer

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def initHand(GameDetails):
    hand_details = HandDetails()
    GameDetails.setInactiveAllPlayers()
    if checkIfDealerSet(GameDetails.getPlayers()):
        initDealer(GameDetails.getPlayers())
    else:
        advanceDealer(GameDetails.getPlayers())
    return hand_details
