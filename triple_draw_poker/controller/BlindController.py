from triple_draw_poker.controller.PlayerController import getDealer

from triple_draw_poker.model.GameDetails import GameDetails

def postBlinds(GameDetails):
    dealer = getDealer(GameDetails.getPlayers())
