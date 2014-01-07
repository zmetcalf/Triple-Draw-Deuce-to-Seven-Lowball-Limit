def getWinner():
    # Must handle receiving differnt lengths of lists...
    return True

def checkIfSuited(card_list):
    last_card = card_list[0].getSuit()
    for card in card_list:
        if last_card != card.getSuit():
            return False
    return True

def checkIfWheel(card_list):
    return False
