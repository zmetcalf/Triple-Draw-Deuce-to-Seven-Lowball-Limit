from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class GameController:

    def __init__(self):
        self.game_details = GameDetails()
        self.hand_details = HandDetails(self.game_details)

    def getButtons():
        # Returns buttons user may use
        return False

    def getTableInfo():
        # Returns dealer button, active player, BR, pot
        return False

    def getPlayer():
        # Returns player details
        return False

    def fold():
        # Handles fold input from user
        return False

    def check():
        # Handles check input from user
        return False

    def call():
        # Handles call input from user
        return False

    def raiseBet():
        # Handels raise input from user
        return False
