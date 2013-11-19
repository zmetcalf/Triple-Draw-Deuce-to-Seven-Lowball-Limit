class Pot:

    def __init__(self):
        self.pot = 0

    def addBet(self, amount):
        self.pot += amount

    def scoop(self):
        bet_to_send = self.pot
        self.pot = 0
        return bet_to_send

    def getPot(self):
        return self.pot
