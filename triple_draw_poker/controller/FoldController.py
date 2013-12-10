from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def fold(GameDetails, HandDetails):
    GameDetails.getActivePlayer().setOutOfHand()
