from triple_draw_poker.controller.PlayerController import changeActivePlayer, \
      getActivePlayer

def advanceHand(game_details):
    if game_details.getHandDetails().getRaised():
        changeActivePlayer(game_details.getPlayers())
        active_player = getActivePlayer(game_details.getPlayers())
        if active_player.getBetThisStreet() == \
            game_details.getHandDetails().getRaised():
                advanceStreet(game_details)
    else:
        active_player = getActivePlayer(game_details.getPlayers())
        if active_player.getDealerStatus():
            advanceStreet(game_details)
        else:
            changeActivePlayer(game_details.getPlayers())

def advanceStreet(game_details):
    if game_details.getHandDetails().getStreet() < \
        game_details.getHandDetails().getNumberOfStreets() - 1:
            game_details.getHandDetails().incrementStreet()
            game_details.getHandDetails().changeInDraw()
    else:
        return showdown(game_details)

def showdown(game_details):
    # TODO Find Winner
    # TODO Scoop or split pot to winner
    # DO NOT ADVANCE DEALER!!!

    return True
