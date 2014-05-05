from triple_draw_poker.controller.BlindController import postBlinds
from triple_draw_poker.controller.HandController import initDeal
from triple_draw_poker.controller.PlayerController import checkIfDealerSet, \
      initDealer, advanceDealer, setInactiveAllPlayers

def initHand(game_details, cards):
    setInactiveAllPlayers(game_details.getPlayers())
    if checkIfDealerSet(game_details.getPlayers()):
        initDealer(game_details.getPlayers())
    else:
        advanceDealer(game_details.getPlayers())
    postBlinds(game_details)
    initDeal(game_details, cards)
