import pandas as pd
import unittest

import hockeydata.scrape.html_pbp as html_pbp
from hockeydata.scrape.scrape import game_html_pbp

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

    def test_parse_pbp(self):
        try:
            pbp = game_html_pbp(game_id=self.game_id)

        except Exception as e:
            self.fail(str(e))

    def test_event_parsing(self):
        players = {'Home': {'DION PHANEUF': {'id': 8470602, 'number': '3', 'last_name': 'Phaneuf', 'team': 'L.A'},
                            'DREW DOUGHTY': {'id': 8474563, 'number': '8', 'last_name': 'Doughty', 'team': 'L.A'},
                            'ADRIAN KEMPE': {'id': 8477960, 'number': '9', 'last_name': 'Kempe', 'team': 'L.A'},
                            'ANZE KOPITAR': {'id': 8471685, 'number': '11', 'last_name': 'Kopitar', 'team': 'L.A'},
                            'KYLE CLIFFORD': {'id': 8475160, 'number': '13', 'last_name': 'Clifford', 'team': 'L.A'},
                            'BRENDAN LEIPSIC': {'id': 8476894, 'number': '14', 'last_name': 'Leipsic', 'team': 'L.A'},
                            'ILYA KOVALCHUK': {'id': 8469454, 'number': '17', 'last_name': 'Kovalchuk', 'team': 'L.A'},
                            'ALEX IAFALLO': {'id': 8480113, 'number': '19', 'last_name': 'Iafallo', 'team': 'L.A'},
                            'TREVOR LEWIS': {'id': 8473453, 'number': '22', 'last_name': 'Lewis', 'team': 'L.A'},
                            'DUSTIN BROWN': {'id': 8470606, 'number': '23', 'last_name': 'Brown', 'team': 'L.A'},
                            'DEREK FORBORT': {'id': 8475762, 'number': '24', 'last_name': 'Forbort', 'team': 'L.A'},
                            'AUSTIN WAGNER': {'id': 8478455, 'number': '51', 'last_name': 'Wagner', 'team': 'L.A'},
                            'KURTIS MACDERMID': {'id': 8477073, 'number': '56', 'last_name': 'MacDermid', 'team': 'L.A'},
                            'SEAN WALKER': {'id': 8480336, 'number': '61', 'last_name': 'Walker', 'team': 'L.A'},
                            'TYLER TOFFOLI': {'id': 8475726, 'number': '73', 'last_name': 'Toffoli', 'team': 'L.A'},
                            'JONNY BRODZINSKI': {'id': 8477380, 'number': '76', 'last_name': 'Brodzinski', 'team': 'L.A'},
                            'JEFF CARTER': {'id': 8470604, 'number': '77', 'last_name': 'Carter', 'team': 'L.A'},
                            'MATT ROY': {'id': 8478911, 'number': '81', 'last_name': 'Roy', 'team': 'L.A'},
                            'JONATHAN QUICK': {'id': 8471734, 'number': '32', 'last_name': 'Quick', 'team': 'L.A'},
                            'PAUL LADUE': {'id': 8476983, 'number': '2', 'last_name': 'LaDue', 'team': 'L.A'},
                            'ALEC MARTINEZ': {'id': 8474166, 'number': '27', 'last_name': 'Martinez', 'team': 'L.A'}
                            },
                   'Away': {'DUNCAN KEITH': {'id': 8470281, 'number': '2', 'last_name': 'Keith', 'team': 'CHI'},
                            'CONNOR MURPHY': {'id': 8476473, 'number': '5', 'last_name': 'Murphy', 'team': 'CHI'},
                            'BRENT SEABROOK': {'id': 8470607, 'number': '7', 'last_name': 'Seabrook', 'team': 'CHI'},
                            'BRENDAN PERLINI': {'id': 8477943, 'number': '11', 'last_name': 'Perlini', 'team': 'CHI'},
                            'ALEX DEBRINCAT': {'id': 8479337, 'number': '12', 'last_name': 'DeBrincat', 'team': 'CHI'},
                            'CHRIS KUNITZ': {'id': 8470543, 'number': '14', 'last_name': 'Kunitz', 'team': 'CHI'},
                            'ARTEM ANISIMOV': {'id': 8473573, 'number': '15', 'last_name': 'Anisimov', 'team': 'CHI'},
                            'MARCUS KRUGER': {'id': 8475323, 'number': '16', 'last_name': 'Kruger', 'team': 'CHI'},
                            'DYLAN STROME': {'id': 8478440, 'number': '17', 'last_name': 'Strome', 'team': 'CHI'},
                            'JONATHAN TOEWS': {'id': 8473604, 'number': '19', 'last_name': 'Toews', 'team': 'CHI'},
                            'BRANDON SAAD': {'id': 8476438, 'number': '20', 'last_name': 'Saad', 'team': 'CHI'},
                            'DOMINIK KAHUN': {'id': 8480946, 'number': '24', 'last_name': 'Kahun', 'team': 'CHI'},
                            'JOHN HAYDEN': {'id': 8477401, 'number': '40', 'last_name': 'Hayden', 'team': 'CHI'},
                            'GUSTAV FORSLING': {'id': 8478055, 'number': '42', 'last_name': 'Forsling', 'team': 'CHI'},
                            'ERIK GUSTAFSSON': {'id': 8476979, 'number': '56', 'last_name': 'Gustafsson', 'team': 'CHI'},
                            'SLATER KOEKKOEK': {'id': 8476886, 'number': '68', 'last_name': 'Koekkoek', 'team': 'CHI'},
                            'PATRICK KANE': {'id': 8474141, 'number': '88', 'last_name': 'Kane', 'team': 'CHI'},
                            'DYLAN SIKURA': {'id': 8478106, 'number': '95', 'last_name': 'Sikura', 'team': 'CHI'},
                            'COREY CRAWFORD': {'id': 8470645, 'number': '50', 'last_name': 'Crawford', 'team': 'CHI'},
                            'CARL DAHLSTROM': {'id': 8477472, 'number': '63', 'last_name': 'Dahlstrom', 'team': 'CHI'},
                            'DRAKE CAGGIULA': {'id': 8479465, 'number': '91', 'last_name': 'Caggiula', 'team': 'CHI'}
                            }
                   }
        description = "L.A #23 BROWN(15), Wrist, Off. Zone, 6 ft.Assists: #8 DOUGHTY(30); #32 QUICK(2)"
        player_1 = html_pbp.get_event_player_1(description, 'GOAL', 'L.A', players)
        player_2 = html_pbp.get_event_player_2(description, 'GOAL', players)
        player_3 = html_pbp.get_event_player_3(description, 'GOAL', players)
        self.assertEqual(player_1, 8470606) # brown
        self.assertEqual(player_2, 8474563) # doughty
        self.assertEqual(player_3, 8471734) # quick

        description = "L.A #9 KEMPE Tripping(2 min), Def. Zone Drawn By: CHI #88 KANE"
        player_1 = html_pbp.get_event_player_1(description, 'PENL', 'L.A', players)
        player_2 = html_pbp.get_event_player_2(description, 'PENL', players)
        player_3 = html_pbp.get_event_player_3(description, 'PENL', players)
        self.assertEqual(player_1, 8477960) # KEMPE
        self.assertEqual(player_2, 8474141) # KANE
        self.assertEqual(player_3, None) # none

        description = "CHI ONGOAL - #17 STROME, Snap, Off. Zone, 41 ft."
        player_1 = html_pbp.get_event_player_1(description, 'SHOT', 'CHI', players)
        player_2 = html_pbp.get_event_player_2(description, 'SHOT', players)
        player_3 = html_pbp.get_event_player_3(description, 'SHOT', players)
        self.assertEqual(player_1, 8478440) # STROME
        self.assertEqual(player_2, None) # none
        self.assertEqual(player_3, None) # none

        # TODO
        description = "CHI TEAM Too many men/ice - bench(2 min) Served By: #95 SIKURA, Neu. Zone"

        """
        description = "BOS won Off. Zone - N.J #19 ZAJAC vs BOS #55 ACCIARI"
        player_1 = html_pbp.get_event_player_1(description, 'FAC', 'CHI', players)
        player_2 = html_pbp.get_event_player_2(description, 'SHOT', players)
        player_3 = html_pbp.get_event_player_3(description, 'SHOT', players)
        self.assertEqual(player_1, 8478440) # STROME
        self.assertEqual(player_2, None) # none
        self.assertEqual(player_3, None) # none
        """

