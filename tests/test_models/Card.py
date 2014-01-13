# This is a model for testing only to remove pygame requirement

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # SPADE CLUB DIAMOND HEART

    def getSuit(self):
        return self.suit

    # 1, 2, 3...12, 13

    def getRank(self):
        return self.rank

    def setRank(self, rank): # TODO Need to refactor real class
        self.rank = rank
