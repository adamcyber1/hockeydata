"""
Functions for parsing the JSON play by play data
"""

from json import loads
import pandas as pd
from pandas import DataFrame
from operator import itemgetter

from hockeydata.constants import NHLAPI
from hockeydata.scrape.common import fix_team, get_page, to_seconds, fix_name, safeget

#these transformations are applied to make sure the naming is consistent between this source and the HTML source
event_types = {
    'PERIOD START': 'PSTR',
    'FACEOFF': 'FAC',
    'BLOCKED SHOT': 'BLOCK',
    'BLOCKED_SHOT': 'BLOCK',
    'GAME END': 'GEND',
    'GIVEAWAY': 'GIVE',
    'GOAL': 'GOAL',
    'HIT': 'HIT',
    'MISSED SHOT': 'MISS',
    'MISSED_SHOT': 'MISS',
    'PERIOD END': 'PEND',
    'SHOT': 'SHOT',
    'STOPPAGE': 'STOP',
    'TAKEAWAY': 'TAKE',
    'PENALTY': 'PENL',
    'EARLY INT START': 'EISTR',
    'EARLY INT END': 'EIEND',
    'SHOOTOUT COMPLETE': 'SOC',
    'CHALLENGE': 'CHL',
    'EMERGENCY GOALTENDER': 'EGPID'
}

def change_event_name(event):
    return event_types.get(event.upper(), event)

def scrape_game(game_id: str) -> DataFrame:
    raw_json = get_raw_json(game_id)
    df = parse_json(raw_json)
    return df

def get_raw_json(game_id: str) -> dict:
    url = NHLAPI + 'game/{}/feed/live'.format(game_id)
    res = get_page(url)

    try:
        json_res = loads(res)
        return json_res
    except Exception:
        return None

def parse_event(event) -> dict:
    play = dict()

    play['EVENT_INDEX'] = event['about']['eventIdx']
    play['PERIOD'] = event['about']['period']
    play['EVENT_TYPE'] = str(change_event_name(event['result']['event']))
    play['GAME_SECONDS'] = to_seconds(event['about']['periodTime'])

    # If there's a players key that means an event occurred on the play.
    if 'players' in event.keys():
        play['EVENT_PLAYER_1_NAME'] = fix_name(event['players'][0]['player']['fullName'])
        play['EVENT_PLAYER_1_ID'] = event['players'][0]['player']['id']

        for i in range(len(event['players'])):
            if event['players'][i]['playerType'] != 'Goalie':
                play['EVENT_PLAYER_{}_NAME'.format(i + 1)] = fix_name(event['players'][i]['player']['fullName'].upper())
                play['EVENT_PLAYER_{}_ID'.format(i + 1)] = event['players'][i]['player']['id']

        play['X_CORD'] = event['coordinates'].get('x')
        play['Y_CORD'] = event['coordinates'].get('y')

    return play

def parse_json(game_json: dict) -> DataFrame:
    columns = ['PERIOD', 'EVENT_INDEX', 'EVENT_TYPE', 'GAME_SECONDS', 'EVENT_PLAYER_1_NAME', 'EVENT_PLAYER_1_ID', 'EVENT_PLAYER_2_NAME',
               'EVENT_PLAYER_2_ID', 'EVENT_PLAYER_3_NAME', 'EVENT_PLAYER_3_ID', 'X_CORD', 'Y_CORD']

    events_to_ignore = ['PERIOD READY', 'PERIOD OFFICIAL', 'GAME READY', 'GAME OFFICIAL', 'GAME SCHEDULED']

    try:
        plays = game_json['liveData']['plays']['allPlays']
        events = [parse_event(play) for play in plays if play['result']['event'].upper() not in events_to_ignore]
        sorted_events = sorted(events, key=itemgetter('EVENT_INDEX'))
        return pd.DataFrame(sorted_events, columns=columns)
    except Exception as e:
        return None

def get_teams(game_id: str) -> dict:
    """
    Returns the teams involved in 'game_id'

    :param game_id:
    :return: dict of teams associated with this game_id : {'Home': 'ABC', 'Away': 'XYZ'}
    """
    try:
        raw_json = get_raw_json(game_id)
        return {
            'HOME': fix_team(safeget(raw_json, 'gameData', 'teams', 'home', 'name').upper()),
            'AWAY': fix_team(safeget(raw_json, 'gameData', 'teams', 'away', 'name').upper())
        }

    except Exception as e:
        return None

