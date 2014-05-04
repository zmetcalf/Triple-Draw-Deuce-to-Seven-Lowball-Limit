from triple_draw_poker.controller.PlayerController import getPlayersInHand

def fold(game_details):
    game_details.getActivePlayer().setOutOfHand()
    if getPlayersInHand(GameDetails.getPlayers()) == 1:
        return # Showdown - write later
    # Call advance hand - next player or street
