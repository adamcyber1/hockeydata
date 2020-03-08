"""
This module contains functions to scrape the json schedule for any games or date range
"""

import time
from datetime import datetime

from json import loads

from hockeydata.constants import NHLAPI
import hockeydata.scrape.common as common

def get_date(game_id: str) -> str:

    date_from = '-'.join([game_id[:4], '9', '1'])
    year_to = game_id[:4]

    if year_to == get_season(datetime.strftime(datetime.today(), "%Y-%m-%d")):
        date_to = '-'.join([str(datetime.today().year), str(datetime.today().month), str(datetime.today().day)])
    else:
        date_to = '-'.join([str(int(year_to) + 1), '7', '1'])  # Newest game in sample

    schedule = scrape_schedule(date_from, date_to, preseason=True)

    # Only return games we want in range
    for game in schedule:
        if str(game['GAME_ID']) == game_id:
            return game['DATE']

    return None


def get_dates(games):
    """
    Given a list game_ids it returns the dates for each game.

    We go from the beginning of the earliest season in the sample to the end of the most recent

    :param games: list with game_id's ex: 2016020001

    :return: list with game_id and corresponding date for all games
    """

    # Convert to str to avoid issues
    games = list(map(str, games))

    # Determine oldest and newest game
    games.sort()

    date_from = '-'.join([games[0][:4], '9', '1'])
    year_to = games[-1][:4]

    if year_to == get_season(datetime.strftime(datetime.today(), "%Y-%m-%d")):
        date_to = '-'.join([str(datetime.today().year), str(datetime.today().month), str(datetime.today().day)])
    else:
        date_to = '-'.join([str(int(year_to) + 1), '7', '1'])  # Newest game in sample

    schedule = scrape_schedule(date_from, date_to, preseason=True)

    # Only return games we want in range
    games_list = []
    for game in schedule:
        if str(game['game_id']) in games:
            games_list.extend([game])

    return games_list

def get_schedule_game_ids(date_from, date_to, preseason=False) -> list:
    raw_games = scrape_schedule(date_from, date_to, preseason)
    game_ids = [str(raw_game['GAME_ID']) for raw_game in raw_games]

    return game_ids


def scrape_schedule(date_from, date_to, preseason=False):
    games = []
    raw = get_raw_json(date_from, date_to)
    dates = raw['dates']

    for day in dates:
        if 'games' not in day:
            print("uh oh")

        for game in day['games']:
            game_id = int(str(game['gamePk'])[5:])

            if (game_id >= 20000 or preseason) and game_id < 40000:
                games.append({"GAME_ID": game['gamePk'],
                                 "DATE": day['date'],
                                 "START_TIME": datetime.strptime(game['gameDate'][:-1], "%Y-%m-%dT%H:%M:%S"),
                                 "VENUE": game['venue'].get('name'),
                                 "HOME_TEAM": common.fix_team(game['teams']['home']['team']['name'].upper()),
                                 "AWAY_TEAM": common.fix_team(game['teams']['away']['team']['name'].upper()),
                                 "HOME_SCORE": game['teams']['home'].get("score"),
                                 "AWAY_SCORE": game['teams']['away'].get("score"),
                                 "STATUS": game["status"]["abstractGameState"]
                                 })

    return games


def get_raw_json(date_from: str, date_to: str):
    """
    Get the raw JSON for a date range

    :param date_from:
    :param date_to:
    :return:
    """
    url = NHLAPI + 'schedule?startDate={}&endDate={}'.format(date_from, date_to)
    res = common.get_page(url)

    try:
        json_res = loads(res)
        return json_res
    except Exception as e:
        # log exception
        return None

def get_season(date: str) -> int:
    """
    Get Season based on date

    :param date: date

    :return: season -> ex: 2016 for 2016-2017 season
    """
    year = date[:4]
    date = time.strptime(date, "%Y-%m-%d")

    if time.strptime('-'.join([year, '01-01']), "%Y-%m-%d") <= date <= time.strptime('-'.join([year, '08-01']), "%Y-%m-%d"):
        return int(year) - 1
    else:
        return int(year)