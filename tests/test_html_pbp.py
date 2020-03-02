import pandas as pd
import unittest

import hockeydata.scrape.html_pbp as html_pbp

#TODO get can actual example with an expected output

class TestHTMLPBP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game_id = '2018021000'

    def test_raw_html(self):
        try:
            res = html_pbp.get_raw_html(self.game_id)
        except Exception as e:
            self.fail("get_raw_html() returned unexpected exception: {}".format(str(e)))

    def test_clean_html(self):
        try:
            html = html_pbp.get_raw_html(self.game_id)
            clean_html = html_pbp.clean_html(html)
        except Exception as e:
            self.fail("get_raw_html()+clean_html() returned unexpected exception: {}".format(str(e)))
