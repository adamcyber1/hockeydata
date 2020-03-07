    import pandas as pd
    import unittest

    import hockeydata.scrape.json_schedule as schedule

    class TestSchedule(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.game_id = '2018021000'
            cls.start = '2018-02-02'
            cls.end = '2018-07-02'

        def test_get_date(self):
            try:
                date = schedule.get_date(self.game_id)
                self.assertEqual(date, '2019-03-02')
            except Exception as e:
                self.fail("get_date() returned unexpected exception: {}".format(str(e)))

        def test_scrape_schedule(self):
            try:
                games = schedule.scrape_schedule(self.start, self.end)
                self.assertEqual(569, len(games))

            except Exception as e:
                self.fail("get_scrape_schedule() returned unexpected exception: {}".format(str(e)))