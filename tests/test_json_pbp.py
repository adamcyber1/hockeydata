import pandas as pd
import unittest

import hockeydata.scrape.json_pbp as json_pbp

#TODO get can actual example with an expected output

class TestJSONPBP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game_id = '2018021000'

    def test_raw_html(self):
        try:
            res = json_pbp.scrape_game(self.game_id)
        except Exception as e:
            self.fail("scrape_game() returned unexpected exception: {}".format(str(e)))
