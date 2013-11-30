from triple_draw_poker.controller.ButtonController import getButtons
from triple_draw_poker.controller.InitController import initHand
from triple_draw_poker.controller.RaiseController import raiseBet
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class GameController:

    def __init__(self):
        self.game_details = GameDetails()
        self.hand_details = HandDetails()

    def setupHand(self, GameDetails, HandDetails):
        # Receives data from user screen
        initHand(self.game_details, self.hand_details)

    def getButtons(self):
        return getButtons(self.game_details, self.hand_details)

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
        return raiseBet(self.game_details, self.hand_details)

    def showdown():
        # This may go into call()
        return False
