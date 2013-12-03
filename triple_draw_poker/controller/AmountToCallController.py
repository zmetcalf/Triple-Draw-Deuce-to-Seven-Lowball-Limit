from triple_draw_poker.controller.PlayerController import getActivePlayer

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def getAmountToCall(GameDetails, HandDetails):
    player_to_check = getActivePlayer(GameDetails.getPlayers())
    amount_to_call = HandDetails.getRaised() - player_to_check.getBetThisHand()
    return amount_to_call
