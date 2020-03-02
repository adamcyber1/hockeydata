import hockeydata.scrape.html_roster as roster

import unittest

class TestHTMLRoster(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game_id = '2018021000'

    def test_get_roster(self):
        try:
            res = roster.get_roster(self.game_id)
        except Exception as e:
            self.fail("get_roster() returned unexpected exception: {}".format(str(e)))