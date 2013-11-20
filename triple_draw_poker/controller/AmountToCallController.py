from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

def getAmountToCall(GameDetails, HandDetails):
    for player in GameDetails.getPlayers():
        if player.getActiveStatus:
            player_to_check = player
            break
    amount_to_call = HandDetails.getRaised - player_to_check
    return amount_to_call
