def getWinner():
    # Must handle receiving differnt lengths of lists...
    return True

def getBestHand(hand_one, hand_two):
    rank_function_list = [
        checkIfRoyalFlush,
        checkIfStraightFlush,
        checkIfFourOfKind,
        checkIfFullHouse,
        checkIfThreeOfKind,
        checkIfTwoPaired,
        checkIfPaired,
    ]
    for check in rank_function_list:
        if check(hand_one) and check(hand_two):
            narrowBestHand(hand_one, hand_two, check)
        elif check(hand_one):
            return 'one'
        elif check(hand_two):
            return 'two'
    return False

def narrowBestHand(hand_one, hand_two, rank_cb):
    return True # Used if simple solve from getBestHand cannot be used

def getAceHighList(card_list):
    ace_high_list = card_list
    for card in ace_high_list:
        if card.getRank() == 1:
            card.setRank(14)
    return ace_high_list

def checkIfRoyalFlush(card_list):
    if checkIfBroadway(card_list) and checkIfSuited(card_list):
        return True
    return False

def checkIfStraightFlush(card_list):
    if checkIfStraight(card_list) and checkIfSuited(card_list):
        return checkIfStraight(card_list)
    return False

def checkIfFourOfKind(card_list):
    ace_high_list = getAceHighList(card_list)
    rank_list = []
    for card in ace_high_list:
        rank_list.append(card.getRank())
    if rank_list.count(rank_list[0]) == 4:
        return rank_list[0]
    if rank_list.count(rank_list[1]) == 4:
        return rank_list[1]
    return False

def checkIfFullHouse(card_list):
    ace_high_list = getAceHighList(card_list)
    triplet = checkIfThreeOfKind(ace_high_list)
    pair = checkIfPaired(ace_high_list)
    if not triplet or not pair:
        return False
    return [triplet, pair]

def checkIfThreeOfKind(card_list):
    ace_high_list = getAceHighList(card_list)
    rank_list = []
    for card in ace_high_list:
        rank_list.append(card.getRank())
    for rank in rank_list:
        if rank_list.count(rank) == 3:
            return rank
    return False

def checkIfTwoPaired(card_list):
    ace_high_list = getAceHighList(card_list)
    rank_list = []
    pairs = []
    kicker = 0
    for card in ace_high_list:
        rank_list.append(card.getRank())
    for rank in rank_list:
        if rank_list.count(rank) == 2:
            if not pairs.count(rank):
                pairs.append(rank)
        else:
            kicker = rank
    if len(pairs) == 2:
        pairs.sort()
        pairs.append(kicker) # Kicker is last
        return pairs
    return False

def checkIfPaired(card_list):
    ace_high_list = getAceHighList(card_list)
    rank_list = []
    for card in ace_high_list:
        rank_list.append(card.getRank())
    for rank in rank_list:
        if rank_list.count(rank) == 2:
            return rank
    return False

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
