import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.model.Pot import Pot

class PotTests(unittest.TestCase):
    def setUp(self):
        self.pot = Pot()

    def testGetPot(self):
        self.assertEqual(self.pot.getPot(), 0)

    def testAddBet(self):
        self.pot.addBet(10)
        self.assertEqual(self.pot.getPot(), 10)

    def testScoop(self):
        self.pot.addBet(10)
        self.assertEqual(self.pot.scoop(), 10)
        self.assertEqual(self.pot.getPot(), 0)

if __name__ == '__main__':
    unittest.main()
