from triple_draw_poker.controller.PlayerController import changeActivePlayer, \
      getActivePlayer

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def advanceHand(HandDetails, GameDetails):
    active_player = getActivePlayer(GameDetails.getPlayers())
    if HandDetails.getRaised():
        changeActivePlayer(GameDetails.getPlayers())
        if active_player.getBetThisStreet() == HandDetails.getRaised():
            advanceStreet(HandDetails)
    else:
        if active_player.getDealerStatus():
            advanceStreet(HandDetails)
        else:
            changeActivePlayer(GameDetails.getPlayers())

def advanceStreet(HandDetails):
    if HandDetails.getStreet() < HandDetails.getNumberOfStreets() - 1:
        HandDetails.incrementStreet()
        # TODO Engage Draw
    else:
        return 'Showdown'
