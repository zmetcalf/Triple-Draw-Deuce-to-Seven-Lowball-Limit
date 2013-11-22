import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.model.HandDetails import HandDetails

class HandDetailsTests(unittest.TestCase):
    def setUp(self):
        self.hand_details = HandDetails()

    def testGetPot(self):
        self.assertEqual(self.hand_details.getPot(), 0)

if __name__ == '__main__':
    unittest.main()

