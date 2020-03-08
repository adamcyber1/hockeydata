"""
Functions for parsing the JSON boxscore
"""

from json import loads

import pandas as pd
from pandas import DataFrame

import hockeydata.scrape.common as common
from hockeydata.scrape.json_schedule import get_date
from hockeydata.constants import GAME_INFO_COLUMNS, NHLAPI_URL


def scrape_game(game_id: str) -> DataFrame:
    raw_json = get_raw_json(game_id)
    df = parse_json(raw_json)

    return df

def get_raw_json(game_id: str) -> dict:
    """
    Given a game_id it returns the raw json
    :param game_id: the game

    :return: json or None
    """
    url = NHLAPI_URL +  'game/' + game_id + '/boxscore'
    res = common.get_page(url)

    try:
        json_res = loads(res)
        json_res['GAME_ID'] = game_id #boxscore doesnt have the game_id anywhere...and i want my function calls to be clean
        return json_res
    except Exception as e:
        # log exception
        return None

def parse_json(game_json: dict) -> DataFrame:
    """
GAME_INFO = ['GAME_ID', 'GAME_DATE', 'HOME_TEAM_ID', 'HOME_TEAM_FULL_NAME', 'AWAY_TEAM_ID', 'AWAY_TEAM_FULL_NAME',
             'HOME_GOALS', 'AWAY_GOALS', 'RESULT', 'HOME_SHOTS', 'AWAY_SHOTS']
"""
    # first create a dict, then coerce it into a df. Better ways to do this? Probably.
    record = pd.Series(index=GAME_INFO_COLUMNS)
    record.GAME_ID = game_json['GAME_ID']
    record.GAME_DATE = get_date(game_json['GAME_ID'])
    record.HOME_TEAM_ID = game_json['teams']['home']['team']['id']
    record.HOME_TEAM_FULL_NAME = game_json['teams']['home']['team']['name']
    record.AWAY_TEAM_ID = game_json['teams']['away']['team']['id']
    record.AWAY_TEAM_FULL_NAME = game_json['teams']['away']['team']['name']
    record.HOME_GOALS = game_json['teams']['home']['teamStats']['teamSkaterStats']['goals']
    record.AWAY_GOALS = game_json['teams']['away']['teamStats']['teamSkaterStats']['goals']
    record.RESULT = 'HOME_WIN' if record.HOME_GOALS > record.AWAY_GOALS else 'AWAY_WIN'
    record.HOME_SHOTS= game_json['teams']['home']['teamStats']['teamSkaterStats']['shots']
    record.AWAY_SHOTS= game_json['teams']['away']['teamStats']['teamSkaterStats']['shots']

    items = record.items()
    col = record.index

    df = DataFrame(columns=GAME_INFO_COLUMNS)
    df = df.append(record, ignore_index=True)

    return df


