from triple_draw_poker.controller.PlayerController import changeActivePlayer, \
        getActivePlayer, getDealer, playerBet

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def postBlinds(GameDetails, HandDetails):
    if len(GameDetails.getPlayers()) > 2:
        changeActivePlayer(GameDetails.getPlayers()) # Dealer posts SB Heads-Up
    getActivePlayer(GameDetails.getPlayers()).setIsSB()
    playerBet(HandDetails, GameDetails.getPlayers(),
              GameDetails.getBetLevel() * 0.5, 0)

    changeActivePlayer(GameDetails.getPlayers())
    getActivePlayer(GameDetails.getPlayers()).setIsBB()
    playerBet(HandDetails, GameDetails.getPlayers(),
              GameDetails.getBetLevel(), 0)

    HandDetails.incrementRaised()

    changeActivePlayer(GameDetails.getPlayers())
