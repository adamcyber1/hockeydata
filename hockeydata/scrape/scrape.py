"""
Game scraping functions - ties together the other scraping modules.
"""
import logging

import pandas as pd
from pandas import DataFrame

from hockeydata.constants import PBP_COLUMNS_ENHANCED
from hockeydata.scrape.json_schedule import get_date, get_schedule_game_ids
from hockeydata.scrape.players import get_players
from hockeydata.scrape import json_shifts, json_pbp, html_pbp, json_boxscore

logger = logging.getLogger('LOG.scrape')

def get_games(start: str, end: str) -> DataFrame:
    """
    Get the game ids for games that occured in the given time range (inclusive)


    :param start: YYYY-MM-DD
    :param end: YYYY-MM-DD
    :return: Dataframe of game ids
    """
    game_ids = get_schedule_game_ids(start, end, False)
    return DataFrame(columns=['GAME_ID'], data=game_ids)


def get_game_summaries(game_ids: list) -> DataFrame:
    summaries = []
    for game_id in game_ids:
        current_summary = get_game_summary(game_id)
        if current_summary is not None:
            summaries.append(current_summary)

    if len(summaries) > 0:
        return pd.concat(summaries)
    else:
        return None

def get_game_summary(game_id: str) -> DataFrame:
    game_summary = json_boxscore.scrape_game(game_id)

    return game_summary


def get_season_pbp(season: int) -> DataFrame:
    logger.info("Scraping Season: {}".format(season))

    from_date = '-'.join([str(season), '9', '1'])
    to_date = '-'.join([str(season + 1), '7', '1'])

    game_ids = get_schedule_game_ids(from_date, to_date, False)

    return get_games_pbp(game_ids)


def get_seasons_pbp(seasons: list) -> DataFrame:
    """

    :param seasons:
    :return:
    """
    logger.info("Scraping PBP of List of Games of Size: {}".format(len(seasons)))

    pbps = []

    for season in seasons:
        current_pbp = get_season_pbp(season)
        if current_pbp is not None:
            pbps.append(current_pbp)

    if len(pbps) > 0:
        return pd.concat(pbps)
    else:
        return None


def get_game_pbp(game_id: str) -> DataFrame:
    """
    Gets the pbp for a game, merges data sources as required.

    :param game_id:
    :return:
    """

    logger.info("Scraping Game: {}".format(game_id))
    pbp = game_html_pbp(game_id)
    pbp = add_event_coordinates(pbp, game_id)

    return pbp

def get_games_pbp(game_ids: list) -> DataFrame:
    """
    Gets the pbp for a list of games. This function is just in charge of merging the output
    from get_game_pbp()

    :param game_ids:
    :return:
    """
    logger.info("Scraping PBP of List of Games of Size: {}".format(len(game_ids)))

    pbps = []

    for game_id in game_ids:
        current_pbp = get_game_pbp(game_id)
        if current_pbp is not None:
            pbps.append(current_pbp)

    if len(pbps) > 0:
        return pd.concat(pbps)
    else:
        return None


def get_game_shifts(game_id: str) -> DataFrame:
    """
    Gets the shifts for a game, tries the JSON api then the HTML source.

    :param game_id:
    :return: Dataframe of shifts for single game
    """
    logger.info("Scraping Shifts of Game: {}".format(game_id))


    shifts = get_json_shifts(game_id)

    return shifts

def get_games_shifts(game_ids: list) -> DataFrame:
    """
    Gets the shifts for list of games and returns a single merged dataframe

    :param game_ids:
    :return: Merged Dataframe of Shifts
    """
    logger.info("Scraping Shifts of List of Games of Size: {}".format(len(game_ids)))

    shifts = []

    for game_id in game_ids:
        current_shifts = get_json_shifts(game_id)
        if current_shifts is not None:
            shifts.append(current_shifts)

    if len(shifts) > 0:
        return pd.concat(shifts)
    else:
        return None



def game_html_pbp(game_id: str) -> DataFrame:
    """
    Gets the play by play data from HTMLREPORTS.

    Note: No coordinate data, call merge() to merge espn/json data.

    :param game_id:
    :return:
    """
    players = get_players(game_id)
    teams = json_pbp.get_teams(game_id)

    pbp = html_pbp.scrape_game(game_id, players, teams)

    return pbp


def get_json_pbp(game_id: str) -> DataFrame:
    res = json_pbp.scrape_game(game_id)
    return res


def get_json_shifts(game_id: str) -> DataFrame:
    shifts = json_shifts.scrape_game(game_id)
    return shifts


def add_event_coordinates(html_pbp: DataFrame, game_id: str):
    """
    Adds coordinates to the HTML pbp using the JSON pbp.


    :param html_pbp:
    :param game_id:
    :return:
    """
    result = None

    date = get_date(game_id)
    json_pbp = get_json_pbp(game_id)
    if json_pbp is not None:
        result = merge_html_json_pbp(json_pbp, html_pbp, game_id, date)

    if result is not None:
        return result
    else:
        return html_pbp


def merge_html_json_pbp(json_pbp: DataFrame, html_pbp: DataFrame, game_id: str, date: str) -> DataFrame:
    """
    Merges pbp data from the JSON source with the HTML source

    :param json_pbp: JSON pbp Dataframe
    :param html_pbp: HTML pbp Dataframe
    :param game_id:
    :param date:
    :return:
    """
    game_df = DataFrame()

    try:
        json_pbp = json_pbp[['PERIOD', 'EVENT_TYPE', 'GAME_SECONDS', 'EVENT_PLAYER_1_ID', 'X_CORD', 'Y_CORD']]

        # game_df = pd.merge(html_pbp, json_pbp, left_index=True, right_index=True, how='left')

        game_df = pd.merge(html_pbp, json_pbp, left_on=['PERIOD', 'EVENT_TYPE', 'GAME_SECONDS', 'EVENT_PLAYER_1'],
                           right_on=['PERIOD', 'EVENT_TYPE', 'GAME_SECONDS', 'EVENT_PLAYER_1_ID'], how='left')

        # This is always done - because merge doesn't work well with shootouts
        game_df = game_df.drop_duplicates(subset=['PERIOD', 'EVENT_TYPE', 'EVENT_DESCRIPTION', 'GAME_SECONDS'])
    except Exception as e:
        return None

    return pd.DataFrame(game_df, columns=PBP_COLUMNS_ENHANCED)

