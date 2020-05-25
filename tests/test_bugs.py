import unittest

from pandas import DataFrame

from hockeydata import get_play_by_plays
from hockeydata.scrape.scrape import game_html_pbp, get_players

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass


#TODO currently the tests are just doing ball park estimates, it would be nice to have an expected output.


    def test_2018021001(self):
        """
        This game was returning 'None' because of a bug in get_players, where come players in the JSON data do not have
        a 'currentTeam'. Using a 'safeget' on these players to return 'None' as their team fixes it.

        Not sure how this case will be handled if these players actually make it into the game and have some events
        Associated with them, maybe use their linemates to infer their team?
        """
        try:
            players = get_players('2018021001')
            self.assertIsInstance(players, dict)
            self.assertEqual(len(players), 2) # two teams

            res = get_play_by_plays('2018021001')
            self.assertIsInstance(res, DataFrame)
            self.assertGreater(res.shape[0], 200) # just a rough ball-park check for the number of events
            self.assertGreater(res.shape[1], 10) # another rough ball-park check for the number of columns

        except Exception as e:
            self.fail(e)


if __name__ == '__main__':
    unittest.main()