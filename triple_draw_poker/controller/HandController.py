from triple_draw_poker.controller.PlayerController import changeActivePlayer, \
      getActivePlayer

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def advanceHand(HandDetails, GameDetails):
    active_player = getActivePlayer(GameDetails.getPlayers())
    if HandDetails.getRaised():
        changeActivePlayer(GameDetails.getPlayers())
        if active_player.getBetThisStreet() == HandDetails.getRaised():
            return 'Next Street' # TODO activate next street
    else:
        if active_player.getDealerStatus():
            return 'Next Street' # TODO activate next street
        else:
            changeActivePlayer(GameDetails.getPlayers())
