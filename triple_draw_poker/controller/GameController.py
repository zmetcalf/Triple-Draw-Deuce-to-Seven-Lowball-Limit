from triple_draw_poker.controller.ButtonController import getButtons
from triple_draw_poker.controller.InitController import initHand
from triple_draw_poker.controller.RaiseController import raiseBet
from triple_draw_poker.model.GameDetails import GameDetails

class GameController:

    def __init__(self):
        self.game_details = GameDetails()

    def setupHand(self, cards):
        initHand(self.game_details, cards)

    def getButtons(self):
        return getButtons(self.game_details)

    def getTableInfo():
        # Returns dealer button, active player, BR, pot
        pass

    def getPlayer():
        # Returns player details
        pass

    def fold():
        # Handles fold input from user
        pass

    def check():
        # Handles check input from user
        pass

    def call():
        # Handles call input from user
        pass

    def raiseBet():
        raiseBet(self.game_details)

    def showdown():
        # This may go into call()
        return False
