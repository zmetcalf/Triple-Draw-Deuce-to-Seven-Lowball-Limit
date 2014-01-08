def getWinner():
    # Must handle receiving differnt lengths of lists...
    return True

def checkIfSuited(card_list):
    for card in card_list:
        if card_list[0].getSuit() != card.getSuit():
            return False
    return True

def checkIfStraight(card_list):
    if checkIfBroadway(card_list):
        return checkIfBroadway(card_list)
    if checkIfWheel(card_list):
        return checkIfWheel(card_list)

    straight_check_list = []
    for card in card_list:
        straight_check_list.append(card.getRank())
    straight_check_list.sort()
    check_rank = straight_check_list[0]
    for rank in range(1, len(straight_check_list)):
        if check_rank != straight_check_list[rank] - 1:
            return False
        check_rank = straight_check_list[rank]
    return straight_check_list[4]

def checkIfBroadway(card_list):
    straight_check_list = []
    for card in card_list:
        straight_check_list.append(card.getRank())
    straight_check_list.sort()
    if straight_check_list == [1, 10, 11, 12, 13]:
        return 14
    return False

def checkIfWheel(card_list):
    straight_check_list = []
    for card in card_list:
        straight_check_list.append(card.getRank())
    straight_check_list.sort()
    if straight_check_list == [1, 2, 3, 4, 5]:
        return 5
    return False
