from triple_draw_poker.controller.PlayerController import changeActivePlayer, \
        getActivePlayer, getDealer, playerBet

from triple_draw_poker.model.GameDetails import GameDetails

def postBlinds(GameDetails):
    changeActivePlayer(GameDetails.getPlayers())
    getActivePlayer(GameDetails.getPlayers()).setIsSB()
    playerBet(GameDetails.getPlayers(), GameDetails.getBetLevel() * 0.5, 0)

    changeActivePlayer(GameDetails.getPlayers())
    getActivePlayer(GameDetails.getPlayers()).setIsBB()
    playerBet(GameDetails.getPlayers(), GameDetails.getBetLevel(), 0)

    changeActivePlayer(GameDetails.getPlayers())
