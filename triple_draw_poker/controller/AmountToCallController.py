from triple_draw_poker.controller.PlayerController import getActivePlayer

from triple_draw_poker.model.GameDetails import GameDetails

def getAmountToCall(GameDetails):
    player_to_check = getActivePlayer(GameDetails.getPlayers())
    amount_to_call = GameDetails.getHandDetails().getRaised() - \
        player_to_check.getBetThisStreet()
    return amount_to_call
