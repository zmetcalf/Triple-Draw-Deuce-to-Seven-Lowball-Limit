from triple_draw_poker.controller.AmountToCallController import getAmountToCall
from triple_draw_poker.controller.PlayerController import changeActivePlayer, \
    playerBet, setRaiser

def raiseBet(game_details):
    amount_to_call = getAmountToCall(game_details)
    game_details.getHandDetails().incrementRaised()
    setRaiser(game_details.getPlayers())
    playerBet(game_details,
              game_details.getHandDetails().getStreetPremium() *
              game_details.getBetLevel() * (amount_to_call + 1),
              amount_to_call + 1)
    changeActivePlayer(game_details.getPlayers())
