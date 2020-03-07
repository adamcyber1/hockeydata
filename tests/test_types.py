import unittest
from hockeydata.scrape.types import *

class TestTypes(unittest.TestCase):

    def test_player_id(self):
        try:
            id = PlayerID("12345")
            id = PlayerID(1234)
        except Exception as e:
            self.fail("PlayerID() returned unexpected exception: {}".format(str(e)))

        self.assertRaises(TypeError, PlayerID, "ewferfe")
        self.assertRaises(TypeError, PlayerID, [1,23])
