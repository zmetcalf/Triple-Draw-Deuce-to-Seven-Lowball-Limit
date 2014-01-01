from triple_draw_poker.controller.PlayerController import changeActivePlayer, \
      getActivePlayer

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def advanceHand(HandDetails, GameDetails):
    if HandDetails.getRaised():
        changeActivePlayer(GameDetails.getPlayers())
        active_player = getActivePlayer(GameDetails.getPlayers())
        if active_player.getBetThisStreet() == HandDetails.getRaised():
            advanceStreet(HandDetails, GameDetails)
    else:
        active_player = getActivePlayer(GameDetails.getPlayers())
        if active_player.getDealerStatus():
            advanceStreet(HandDetails, GameDetails)
        else:
            changeActivePlayer(GameDetails.getPlayers())

def advanceStreet(HandDetails, GameDetails):
    if HandDetails.getStreet() < HandDetails.getNumberOfStreets() - 1:
        HandDetails.incrementStreet()
        HandDetails.changeInDraw()
    else:
        return showdown(HandDetails, GameDetails)

def showdown(HandDetails, GameDetails):
    # TODO Find Winner
    # TODO Scoop or split pot to winner
    # DO NOT ADVANCE DEALER!!!

    return True
