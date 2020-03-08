import pandas as pd
import unittest

import hockeydata.scrape.json_boxscore as json_boxscore

#TODO get can actual example with an expected output

class TestJSONBoxscore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game_id = '2018021000'

    def test_boxscore(self):
        try:
            res = json_boxscore.scrape_game(self.game_id)

            self.assertEqual(res.iloc[0].GAME_ID, int('2018021000'))
        except Exception as e:
            self.fail("scrape_game() returned unexpected exception: {}".format(str(e)))