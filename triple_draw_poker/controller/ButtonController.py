from triple_draw_poker.controller.AmountToCallController import getAmountToCall

def getButtons(game_details):
    fold = False
    check = True
    call = False
    bet = False
    raiser = False

    if getAmountToCall(game_details):
        call = True
        check = False
        fold = True

    if 0 < game_details.getHandDetails().getRaised() < 4:
        raiser = True
    elif not game_details.getHandDetails().getRaised():
        bet = True

    return [fold, check, call, bet, raiser]
