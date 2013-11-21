from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def getAmountToCall(GameDetails, HandDetails):
    player_to_check = GameDetails.getActivePlayer()
    amount_to_call = HandDetails.getRaised() - player_to_check.getBetThisHand()
    return amount_to_call
