from io import StringIO

import unittest
from unittest.mock import patch
import click
from click.testing import CliRunner

from hockeydata.cli.__main__ import _list_games, _scrape_game

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()
        cls.game_id_1 = '2018021000'
        cls.game_id_2 = '2018021001'

    def test_list_games(self):
        try:
            text_result = self.runner.invoke(_list_games)
            json_result = self.runner.invoke(_list_games, ['--output-format', 'json'])
        except Exception as e:
            self.fail("_list_games() returned unexpected exception: {}".format(str(e)))

    def test_scrape_game(self):
        try:
            text_result = self.runner.invoke(_scrape_game, [self.game_id_1])
            json_result = self.runner.invoke(_scrape_game, ['--output-format', 'json', self.game_id_1, self.game_id_2])
        except Exception as e:
            self.fail("_list_games() returned unexpected exception: {}".format(str(e)))

