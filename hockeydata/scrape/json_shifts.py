"""
Functions for parsing the JSON shift data
"""

from json import loads

import pandas as pd
from pandas import DataFrame

import hockeydata.scrape.common as common
from hockeydata.constants import SHIFTS

def get_raw_json(game_id: str) -> dict:
    """
    Given a game_id it returns the raw json
    :param game_id: the game

    :return: json or None
    """
    url = SHIFTS + game_id
    res = common.get_page(url)

    try:
        json_res = loads(res)
        return json_res
    except Exception as e:
        # log exception
        return None


def fix_team_tricode(tricode):
    """
    :param tricode: 3 letter team name - ex: NYR

    :return: fixed tricode
    """
    fixes = {
        'TBL': 'T.B',
        'LAK': 'L.A',
        'NJD': 'N.J',
        'SJS': 'S.J'
    }

    if tricode.upper() in list(fixes.keys()):
        return fixes[tricode.upper()]
    else:
        return tricode


def parse_shift(shift: dict) -> dict:
    """
    Parse shift for json

    :param shift: json for shift

    :return: dict with shift info
    """
    try:
        shift_dict = dict()

        name = common.fix_name(' '.join([shift['firstName'].strip(' ').upper(), shift['lastName'].strip(' ').upper()]))
        shift_dict['PLAYER'] = name
        shift_dict['PLAYER_ID'] = shift['playerId']
        shift_dict['PERIOD'] = shift['period']
        shift_dict['TEAM'] = fix_team_tricode(shift['teamAbbrev'])

        # goal events have an eventDescription, we dont care about those.
        if shift['eventDescription'] is not 'EVG':
            shift_dict['START'] = common.to_seconds(shift['startTime'])
            shift_dict['END'] = common.to_seconds(shift['endTime'])
            shift_dict['DURATION'] = common.to_seconds(shift['duration'])

            return shift_dict
        else:
            return None
    except Exception as e:
        return None

def parse_json(shift_json: dict, game_id: str):
    """
    Parse the json

    :param shift_json: raw json
    :param game_id: if of game

    :return: DataFrame with info
    """
    columns = ['GAME_ID', 'PERIOD', 'TEAM', 'PLAYER', 'PLAYER_ID', 'START', 'END', 'DURATION']

    shifts = []

    for shift in shift_json['data']:
        current_shift = parse_shift(shift)
        if current_shift is not None:
            shifts.append(current_shift)

    df = pd.DataFrame(shifts, columns=columns)
    df['GAME_ID'] = str(game_id)
    df = df.sort_values(by=['PERIOD', 'START'], ascending=[True, True])  # Sort by period by time
    df = df.reset_index(drop=True)

    return df


def scrape_game(game_id: str) -> DataFrame:
    """
    Do the actual scraping, if something goes wrong just return None.

    :param game_id: game id in statsapi format (i.e. 20018020028)

    :return: DataFrame of shifts data
    """
    shifts_json = get_raw_json(game_id)

    if not shifts_json:
        return None

    try:
        game_df = parse_json(shifts_json, game_id)
    except Exception as e:
        return None

    return game_df