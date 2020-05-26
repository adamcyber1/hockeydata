import unittest

from pandas import DataFrame

from hockeydata import get_play_by_plays
from hockeydata.scrape.scrape import game_html_pbp, get_players
import hockeydata.scrape.html_pbp as html_pbp

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

    def test_event_parsing_2018021001(self):
        """
        When players had changed their number at some point, the JSON data became unreliable. The Player info needs
        to be constructed using the HTMLReport roster, which is the actual day-of data, including jersey numbers.

        'Anderson' was the culprit - changed his number from 49 to 14.

        TODO: Add in Position Data, which is conveniently available form the roster
        http://www.nhl.com/scores/htmlreports/20182019/RO021001.HTM
        """
        players = {'Home': {'CHARLIE COYLE': {'id': 8475745, 'number': '13', 'last_name': 'COYLE', 'team': 'BOS'},
                            'CHRIS WAGNER': {'id': 8475780, 'number': '14', 'last_name': 'WAGNER', 'team': 'BOS'},
                            'JOAKIM NORDSTROM': {'id': 8475807, 'number': '20', 'last_name': 'NORDSTROM',
                                                 'team': 'BOS'},
                            'PETER CEHLARIK': {'id': 8477417, 'number': '22', 'last_name': 'CEHLARIK', 'team': 'BOS'},
                            'BRANDON CARLO': {'id': 8478443, 'number': '25', 'last_name': 'CARLO', 'team': 'BOS'},
                            'JOHN MOORE': {'id': 8475186, 'number': '27', 'last_name': 'MOORE', 'team': 'BOS'},
                            'ZDENO CHARA': {'id': 8465009, 'number': '33', 'last_name': 'CHARA', 'team': 'BOS'},
                            'PATRICE BERGERON': {'id': 8470638, 'number': '37', 'last_name': 'BERGERON', 'team': 'BOS'},
                            'DAVID BACKES': {'id': 8470655, 'number': '42', 'last_name': 'BACKES', 'team': 'ANA'},
                            'DANTON HEINEN': {'id': 8478046, 'number': '43', 'last_name': 'HEINEN', 'team': 'ANA'},
                            'DAVID KREJCI': {'id': 8471276, 'number': '46', 'last_name': 'KREJCI', 'team': 'BOS'},
                            'TOREY KRUG': {'id': 8476792, 'number': '47', 'last_name': 'KRUG', 'team': 'BOS'},
                            'MATT GRZELCYK': {'id': 8476891, 'number': '48', 'last_name': 'GRZELCYK', 'team': 'BOS'},
                            'NOEL ACCIARI': {'id': 8478569, 'number': '55', 'last_name': 'ACCIARI', 'team': 'FLA'},
                            'BRAD MARCHAND': {'id': 8473419, 'number': '63', 'last_name': 'MARCHAND', 'team': 'BOS'},
                            'CHARLIE MCAVOY': {'id': 8479325, 'number': '73', 'last_name': 'MCAVOY', 'team': 'BOS'},
                            'JAKE DEBRUSK': {'id': 8478498, 'number': '74', 'last_name': 'DEBRUSK', 'team': 'BOS'},
                            'MARCUS JOHANSSON': {'id': 8475149, 'number': '90', 'last_name': 'JOHANSSON',
                                                 'team': 'BUF'},
                            'TUUKKA RASK': {'id': 8471695, 'number': '40', 'last_name': 'RASK', 'team': 'BOS'},
                            'STEVEN KAMPFER': {'id': 8474000, 'number': '44', 'last_name': 'KAMPFER', 'team': 'BOS'},
                            'SEAN KURALY': {'id': 8476374, 'number': '52', 'last_name': 'KURALY', 'team': 'BOS'},
                            'KEVAN MILLER': {'id': 8476191, 'number': '86', 'last_name': 'MILLER', 'team': 'BOS'}},
                   'Away': {'CONNOR CARRICK': {'id': 8476941, 'number': '5', 'last_name': 'CARRICK', 'team': 'N.J'},
                            'ANDY GREENE': {'id': 8472382, 'number': '6', 'last_name': 'GREENE', 'team': 'NYI'},
                            'WILL BUTCHER': {'id': 8477355, 'number': '8', 'last_name': 'BUTCHER', 'team': 'N.J'},
                            'NICO HISCHIER': {'id': 8480002, 'number': '13', 'last_name': 'HISCHIER', 'team': 'N.J'},
                            'NICK LAPPIN': {'id': 8479250, 'number': '15', 'last_name': 'LAPPIN', 'team': 'STL'},
                            'STEVEN SANTINI': {'id': 8477463, 'number': '16', 'last_name': 'SANTINI', 'team': 'NSH'},
                            'KENNY AGOSTINO': {'id': 8475844, 'number': '17', 'last_name': 'AGOSTINO', 'team': 'TOR'},
                            'DREW STAFFORD': {'id': 8471226, 'number': '18', 'last_name': 'STAFFORD', 'team': 'UNK'},
                            'TRAVIS ZAJAC': {'id': 8471233, 'number': '19', 'last_name': 'ZAJAC', 'team': 'N.J'},
                            'BLAKE COLEMAN': {'id': 8476399, 'number': '20', 'last_name': 'COLEMAN', 'team': 'T.B'},
                            'DAMON SEVERSON': {'id': 8476923, 'number': '28', 'last_name': 'SEVERSON', 'team': 'N.J'},
                            'MICHAEL MCLEOD': {'id': 8479415, 'number': '41', 'last_name': 'MCLEOD', 'team': 'N.J'},
                            'SAMI VATANEN': {'id': 8475222, 'number': '45', 'last_name': 'VATANEN', 'team': 'CAR'},
                            'JOEY ANDERSON': {'id': 8479315, 'number': '49', 'last_name': 'ANDERSON', 'team': 'N.J'},
                            'BLAKE PIETILA': {'id': 8476370, 'number': '56', 'last_name': 'PIETILA', 'team': 'ANA'},
                            'KEVIN ROONEY': {'id': 8479291, 'number': '58', 'last_name': 'ROONEY', 'team': 'N.J'},
                            'JESPER BRATT': {'id': 8479407, 'number': '63', 'last_name': 'BRATT', 'team': 'N.J'},
                            'EGOR YAKOVLEV': {'id': 8480948, 'number': '74', 'last_name': 'YAKOVLEV', 'team': 'UNK'},
                            'MACKENZIE BLACKWOOD': {'id': 8478406, 'number': '29', 'last_name': 'BLACKWOOD',
                                                    'team': 'N.J'},
                            'KYLE PALMIERI': {'id': 8475151, 'number': '21', 'last_name': 'PALMIERI', 'team': 'N.J'},
                            'MIRCO MUELLER': {'id': 8477509, 'number': '25', 'last_name': 'MUELLER', 'team': 'N.J'},
                            'PAVEL ZACHA': {'id': 8478401, 'number': '37', 'last_name': 'ZACHA', 'team': 'N.J'},
                            'KURTIS GABRIEL': {'id': 8476545, 'number': '39', 'last_name': 'GABRIEL', 'team': 'PHI'},
                            'NATHAN BASTIAN': {'id': 8479414, 'number': '42', 'last_name': 'BASTIAN', 'team': 'N.J'},
                            'MILES WOOD': {'id': 8477425, 'number': '44', 'last_name': 'WOOD', 'team': 'N.J'},
                            'JOHN QUENNEVILLE': {'id': 8477961, 'number': '47', 'last_name': 'QUENNEVILLE',
                                                 'team': 'CHI'}}}

        description = 'N.J won Neu. Zone - N.J #49 ANDERSON vs BOS #46 KREJCI'
        player_1 = html_pbp.get_event_player_1(description, 'FAC', 'N.J', players)
        player_2 = html_pbp.get_event_player_2(description, 'FAC', players)
        player_3 = html_pbp.get_event_player_3(description, 'FAC', players)
        self.assertEqual(player_1, 8479315)  # ANDERSON
        self.assertEqual(player_2, 8471276)  # none
        self.assertEqual(player_3, None)  # none

        description = 'N.J ONGOAL - #16 SANTINI, Wrist, Off. Zone, 28 ft.'
        player_1 = html_pbp.get_event_player_1(description, 'SHOT', 'N.J', players)
        player_2 = html_pbp.get_event_player_2(description, 'SHOT', players)
        player_3 = html_pbp.get_event_player_3(description, 'SHOT', players)
        self.assertEqual(player_1, 8477463)  # SANTINI
        self.assertEqual(player_2, None)  # none
        self.assertEqual(player_3, None)  # none

        description = 'N.J #17 AGOSTINO Interference on goalkeeper(2 min), Off. Zone Drawn By: BOS #40 RASK'
        player_1 = html_pbp.get_event_player_1(description, 'PENL', 'N.J', players)
        player_2 = html_pbp.get_event_player_2(description, 'PENL', players)
        player_3 = html_pbp.get_event_player_3(description, 'PENL', players)
        self.assertEqual(player_1, 8475844)  # AGOSTINO
        self.assertEqual(player_2, 8471695)  # RASK
        self.assertEqual(player_3, None)  # none




if __name__ == '__main__':
    unittest.main()