"""
This module implements the hockeydata API
"""

from pandas import DataFrame

import hockeydata.scrape.scrape as scrape


def get_play_by_plays(*args) -> DataFrame:
    """
    Get the play by play data for a game or list of games.

    Usage:

    get_play_by_plays('2018020028')

    :param args: list of str game_ids (i.e. 2018020028)
    :return: Dataframe with the play by play data
    """
    return scrape.get_games_pbp(list(args))


def get_game_shifts(*args) -> DataFrame:
    """
    Get the shift data for a game or list of games

    Usage:

    get_game_shifts('2018020028')
    :param args: list of str game ids (i.e. 2018020028)
    :return: Dataframe with the shift data
    """
    return scrape.get_games_shifts(list(args))


def get_season_play_by_play(season: int) -> DataFrame:
    """
    Get the play by play data for an entire season

    Usage:

    get_season_play_by_play(2018)

    :param season: year that the target season started in (i.e 2018-2019 -> 2018)
    :return: Dataframe with the season data (i.e.
    """
    return scrape.get_season_pbp(season)

def list_games(start: str, end: str) -> DataFrame:
    """
    Get a list of games in the specified time range

    :param start: beginning of date range (YYYY-MM-DD)
    :param end: end of date range (YYYY-MM-DD)
    :return: Dataframe of game ids
    """
    return scrape.get_games(start, end)

def get_game_infos(*args):
    return scrape.get_game_summaries(list(args))



