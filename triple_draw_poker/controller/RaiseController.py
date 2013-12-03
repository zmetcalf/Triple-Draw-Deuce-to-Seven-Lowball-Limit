from triple_draw_poker.controller.AmountToCallController import \
      getAmountToCall
from triple_draw_poker.controller.PlayerController import playerBet

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def raiseBet(GameDetails, HandDetails):
    amount_to_call = getAmountToCall(GameDetails, HandDetails)
    HandDetails.incrementRaised()
    playerBet(GameDetails.getPlayers(), HandDetails.getStreetPremium() *
                          GameDetails.getBetLevel() * (amount_to_call + 1),
                          amount_to_call + 1)
