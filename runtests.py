import unittest

from tests.AmountToCallController_tests import AmountToCallControllerTests
from tests.ButtonController_tests import ButtonControllerTests
from tests.GameController_tests import GameControllerTests
from tests.InitController_tests import InitControllerTests
from tests.RaiseController_tests import RaiseControllerTests

from tests.GameDetails_tests import GameDetailsTests
from tests.HandDetails_tests import HandDetailsTests
from tests.Pot_tests import PotTests

def suite():
    suite = unittest.TestSuite()

    # Controller Tests

    suite.addTest(AmountToCallControllerTests('testRaisedPot'))

    suite.addTest(ButtonControllerTests('testUnraised'))
    suite.addTest(ButtonControllerTests('testRaised'))
    suite.addTest(ButtonControllerTests('testCapped'))

    suite.addTest(GameControllerTests('testHandDetails'))

    suite.addTest(InitControllerTests('testHeadsUpInit'))

    suite.addTest(RaiseControllerTests('testRaisePot'))

    # Model Tests

    suite.addTest(GameDetailsTests('testGetBetLevel'))
    suite.addTest(GameDetailsTests('testGetNumberOfPlayers'))
    suite.addTest(GameDetailsTests('testAdvanceDealerSimple'))
    suite.addTest(GameDetailsTests('testAdvanceDealerRoundTheBend'))

    suite.addTest(HandDetailsTests('testGetPot'))

    suite.addTest(PotTests('testGetPot'))
    suite.addTest(PotTests('testAddBet'))
    suite.addTest(PotTests('testScoop'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
