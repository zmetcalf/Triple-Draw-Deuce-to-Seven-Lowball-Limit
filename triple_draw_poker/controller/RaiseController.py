from triple_draw_poker.controller.AmountToCallController import \
      getAmountToCall
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def raiseBet(GameDetails, HandDetails):
    amount_to_call = getAmountToCall(GameDetails, HandDetails)
    return False

