from triple_draw_poker.controller.PlayerController import getPlayersInHand

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def fold(GameDetails, HandDetails):
    GameDetails.getActivePlayer().setOutOfHand()
    if getPlayersInHand(GameDetails.getPlayers()) == 1:
        return # Showdown - write later
    # Call advance hand - next player or street
