from triple_draw_poker.controller.PlayerController import changeActivePlayer, \
        getActivePlayer, getDealer, playerBet

def postBlinds(game_details):
    if len(game_details.getPlayers()) > 2:
        changeActivePlayer(game_details.getPlayers()) # Dealer posts SB Heads-Up
    getActivePlayer(game_details.getPlayers()).setIsSB()
    playerBet(game_details, game_details.getBetLevel() * 0.5, 0)

    changeActivePlayer(game_details.getPlayers())
    getActivePlayer(game_details.getPlayers()).setIsBB()
    playerBet(game_details, game_details.getBetLevel(), 0)

    game_details.getHandDetails().incrementRaised()

    changeActivePlayer(game_details.getPlayers())
