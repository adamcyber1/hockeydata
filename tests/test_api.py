import unittest

from pandas import DataFrame

from hockeydata import api

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game_id = '2018021000'


#TODO currently the tests are just doing ball park estimates, it would be nice to have an expected output.

    def test_get_play_by_play(self):
        try:
            res = api.get_play_by_plays(self.game_id)
            self.assertIsInstance(res, DataFrame)
            self.assertGreater(res.shape[0], 200) # just a rough ball-park check for the number of events
            self.assertGreater(res.shape[1], 10) # another rough ball-park check for the number of columns
        except Exception as e:
            self.fail("api.get_play_by_plays() returned unexpected exception: {}".format(str(e)))

    def test_get_game_shifts(self):
        try:
            res = api.get_game_shifts(self.game_id)
            self.assertIsInstance(res, DataFrame)
            self.assertGreater(res.shape[0], 200) # just a rough ball-park check for the number of events
            self.assertGreater(res.shape[1], 3) # another rough ball-park check for the number of columns
        except Exception as e:
            self.fail("api.get_game_shifts() returned unexpected exception: {}".format(str(e)))

    def test_list_games(self):
        try:
            res = api.list_games('2018-02-02', '2018-02-02') # default should grap games for today
            self.assertIsInstance(res, DataFrame)
            self.assertEqual(res.shape[0], 4) # there were 4 games on this date
        except Exception as e:
            self.fail("api.list_games() returned unexpected exception: {}".format(str(e)))

if __name__ == '__main__':
    unittest.main()