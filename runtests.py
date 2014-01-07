import unittest

from tests.AmountToCallController_tests import AmountToCallControllerTests
from tests.BlindController_tests import BlindControllerTests
from tests.ButtonController_tests import ButtonControllerTests
from tests.FoldController_tests import FoldControllerTests
from tests.GameController_tests import GameControllerTests
from tests.HandController_tests import HandControllerTests
from tests.InitController_tests import InitControllerTests
from tests.Lowball27HandRankController_tests import Lowball27HandRankControllerTests
from tests.PlayerController_tests import PlayerControllerTests
from tests.RaiseController_tests import RaiseControllerTests

from tests.GameDetails_tests import GameDetailsTests
from tests.HandDetails_tests import HandDetailsTests
from tests.Pot_tests import PotTests

def suite():
    suite = unittest.TestSuite()

    # Controller Tests

    suite.addTest(AmountToCallControllerTests('testRaisedPot'))

    suite.addTest(BlindControllerTests('testPostBlinds'))
    suite.addTest(BlindControllerTests('testPostBlindsHeadsUp'))

    suite.addTest(ButtonControllerTests('testUnraised'))
    suite.addTest(ButtonControllerTests('testRaised'))
    suite.addTest(ButtonControllerTests('testCapped'))

    suite.addTest(FoldControllerTests('testFold'))

    suite.addTest(GameControllerTests('testHandDetails'))

    suite.addTest(HandControllerTests('testAdvanceHandUnraised'))
    suite.addTest(HandControllerTests('testAdvanceHandRaisedRaiser'))
    suite.addTest(HandControllerTests('testAdvanceHandRaisedCaller'))
    suite.addTest(HandControllerTests('testAdvanceStreet'))

    suite.addTest(InitControllerTests('testHeadsUpInit'))

    suite.addTest(Lowball27HandRankControllerTests('testGetWinner'))
    suite.addTest(Lowball27HandRankControllerTests('testCheckIfSuitedTrue'))
    suite.addTest(Lowball27HandRankControllerTests('testCheckIfSuitedFalse'))

    suite.addTest(PlayerControllerTests('testAdvanceDealerSimple'))
    suite.addTest(PlayerControllerTests('testAdvanceDealerRoundTheBend'))
    suite.addTest(PlayerControllerTests('testSetRaiser'))
    suite.addTest(PlayerControllerTests('testChangeActivePlayerSimple'))
    suite.addTest(PlayerControllerTests('testChangeActivePlayerRoundTheBend'))
    suite.addTest(PlayerControllerTests('testGetPlayersInHand'))

    suite.addTest(RaiseControllerTests('testRaisePot'))

    # Model Tests

    suite.addTest(GameDetailsTests('testGetBetLevel'))
    suite.addTest(GameDetailsTests('testGetNumberOfPlayers'))

    suite.addTest(HandDetailsTests('testGetPot'))

    suite.addTest(PotTests('testGetPot'))
    suite.addTest(PotTests('testAddBet'))
    suite.addTest(PotTests('testScoop'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
