from triple_draw_poker.controller.AmountToCallController import getAmountToCall

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def getButtons(GameDetails, HandDetails):
    fold = False
    check = True
    call = False
    bet = False
    raiser = False

    if getAmountToCall(GameDetails, HandDetails):
        call = True
        check = False
        fold = True

    if 0 < HandDetails.getRaised() < 4:
        raiser = True
    elif not HandDetails.getRaised():
        bet = True

    return [fold, check, call, bet, raiser]
