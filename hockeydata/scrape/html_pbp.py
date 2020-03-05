"""
Functions for parsing the HTML play by play data
"""
import re
import logging

from bs4 import BeautifulSoup, SoupStrainer, ResultSet
import pandas as pd
from pandas import DataFrame
from requests import Response


from hockeydata.constants import HTMLREPORTS, PBP_COLUMNS, HTML_COLUMNS, MAIN_EVENTS
from hockeydata.scrape.json_schedule import get_date
import hockeydata.scrape.common as common
from hockeydata.scrape.common import safeget

logger = logging.getLogger('LOG.html_pbp')


def scrape_game(game_id: str, players: dict, teams: dict) -> DataFrame:
    """
    Scrapes a game.

    :param game_id: game id (stats api format)
    :param players: dict with player info
    :param teams: dict with home and away teams

    :return: DataFrame of game info or None if it fails
    """
    game_html = get_raw_html(game_id)

    if not game_html:
        return None

    game_html = clean_html(game_html)
    if len(game_html) == 0:
        return None

    try:
        game_df = parse_html(game_id, game_html, players, teams)
    except Exception as e:
        return None

    return game_df


def parse_html(game_id: str, raw_events: list, players: dict, teams: dict) -> DataFrame:
    """
    Parse html game pbp

    :param raw_events: Cleaned list of events from HTML, descriptions are still unparsed
    :param players: players in the game from JSON pbp: {'Home': {'RON HAINSEY': {'id': 8468493, 'number': '2', 'last_name': 'HAINSEY'} ...
    :param teams: home and away teams : {'HOME': 'OTT', 'AWAY': 'MTL'}

    :return: DataFrame with info
    """
    home = safeget(teams, 'Home')
    away = safeget(teams, 'Away')

    dataframe = DataFrame(columns=HTML_COLUMNS)

    # each event gets converted to a series then appended to the Dataframe
    for event2 in raw_events:
        if not valid_event(event2):
            continue

        # the only state required to parse an event is the players + teams
        series = pd.Series(parse_event(event2, players, home, away), index=HTML_COLUMNS)

        dataframe = dataframe.append(series, ignore_index=True)


    # post processing, this is where we add stuff that isn't directly parse-able from the html. i.e. scores, classifying
    # events as fenwick/corsi etc..
    # add some columns to our dataframe that we dont directly get from the HTML
    dataframe['AWAY_TEAM'] = away
    dataframe['HOME_TEAM'] = home
    dataframe['GAME_ID'] = game_id
    dataframe['DATE'] = get_date(game_id)
    return dataframe


def clean_html(html) -> list:
    """
    Converts the raw HTML into a list of events

    The HTML PBP has 8 columns:
    ['#', 'Per', 'Str', 'Time:El', 'Event', 'Description', 'AWAY On Ice', 'HOME On Ice']

    get_soup() converts the raw HTML into a bs4.ResultSet of all the HTML elements we are interested in.
    We then group these elements into slices of 8 ahd parse each of their contents.

    :param html: Raw HTML
    :return:
    """
    soup = get_soup(html)

    td = [soup[i:i + 8] for i in range(0, len(soup), 8)]

    cleaned_html = [strip_html(x) for x in td]

    return cleaned_html


def get_soup(game_html: Response) -> ResultSet:

    strainer = SoupStrainer('td', attrs={'class': re.compile(r'bborder')})
    soup = BeautifulSoup(game_html, "lxml", parse_only=strainer)
    soup = soup.find_all("td", {"class": re.compile('.*bborder.*')})

    if len(soup) == 0:
        soup = BeautifulSoup(game_html, "html.parser", parse_only=strainer)
        soup = soup.select('td.+.bborder')

        if len(soup) == 0:
            soup = BeautifulSoup(game_html, "html5lib")
            soup = soup.select('td.+.bborder')

    return soup


def get_raw_html(game_id: str):
    """
    Gets the raw Roster HTML from htmlreports.

    :param game_id:
    :return:
    """
    url = HTMLREPORTS + '{}{}/PL{}.HTM'.format(game_id[:4], int(game_id[:4]) + 1, game_id[4:])
    res = common.get_page(url)

    assert res is not None
    return res


def strip_html(event: list) -> list:
    """
    Converts the raw HTML event into something sensible.
    This can be cleaned up to be more readable.

    The HTML PBP has 8 columns:
      0     1      2        3        4          5              6               7
    ['#', 'Per', 'Str', 'Time', 'Event', 'Description', 'AWAY On Ice', 'HOME On Ice']

    :param event: event in raw HTML

    :return: parse event info
    """

    for y in range(len(event)):
        if y == 3:
            event[y] = event[y].get_text()
            index = event[y].find(':')
            event[y] = event[y][:index+3]
        elif (y == 6 or y == 7) and event[0] != '#':
            baz = event[y].find_all('td')
            bar = [baz[z] for z in range(len(baz)) if z % 4 != 0]

            players = []
            for i in range(len(bar)):
                if i % 3 == 0:
                    try:
                        name = parse_name(bar[i].find('font')['title'])
                        number = bar[i].get_text().strip('\n')
                    except KeyError:
                        name = ''
                        number = ''
                elif i % 3 == 1:
                    if name != '':
                        position = bar[i].get_text()
                        players.append([name, number, position])

            event[y] = players
        else:
            event[y] = event[y].get_text()

    return event


def parse_event(event, players, home, away) -> pd.Series:
    """
    Receives an event and parses it

    ['EVENT_INDEX', 'PERIOD', 'STRENGTH', 'GAME_SECONDS', 'EVENT_TYPE', 'EVENT_DESCRIPTION', 'EVENT_DETAIL',
                'EVENT_ZONE', 'EVENT_TEAM', 'EVENT_PLAYER_1', 'EVENT_PLAYER_2', 'EVENT_PLAYER_3',
                'HOME_ON_1', 'HOME_ON_2', 'HOME_ON_3', 'HOME_ON_4', 'HOME_ON_5', 'HOME_ON_6', 'HOME_ON_7',
                'AWAY_ON_1', 'AWAY_ON_2', 'AWAY_ON_3', 'AWAY_ON_4', 'AWAY_ON_5', 'AWAY_ON_6', 'AWAY_ON_7']

    :param event: event type
    :param players: players in game
    :param home_team: home team
    :param current_score: current score for both teams

    :return: dict with info
    """

    series = pd.Series(index=HTML_COLUMNS)

    series['EVENT_INDEX'] = int(event[0])
    series['PERIOD'] = int(event[1])
    series['STRENGTH'] = event[2]
    series['GAME_SECONDS'] = common.to_seconds(event[3]) # fix this
    series['EVENT_TYPE'] = event[4]
    series['EVENT_DESCRIPTION'] = event[5]
    series['EVENT_DETAIL'] = None
    series['EVENT_ZONE'] = get_zone(event[5])
    series['EVENT_TEAM'] = get_event_team(event[5], event[4])

    series['EVENT_PLAYER_1'] = get_event_player_1(event[5], event[4], series.EVENT_TEAM, players)
    series['EVENT_PLAYER_2'] = get_event_player_2(event[5], event[4], players)
    series['EVENT_PLAYER_3'] = get_event_player_3(event[5], event[4], players)

    away_players = event[6]
    for i in range(1, len(away_players) + 1):
        player =  players['Away'].get(away_players[i - 1][0])
        if player is not None:
            series['AWAY_ON_{}'.format(i)] = player.get('id')

    home_players = event[7]
    for i in range(1, len(home_players) + 1):
        player =  players['Home'].get(home_players[i - 1][0])
        if player is not None:
            series['HOME_ON_{}'.format(i)] = player.get('id')

    return series

def get_event_team(event_description: str, event_type: str) -> str:
    """
    Add event team for event

    :param event_dict: dict of event info
    :param event: list with parsed event info

    :return: None
    """
    if event_type in MAIN_EVENTS:
        try:
            pattern = re.compile('^[A-Z]\\.[A-Z]|^[A-Z]+')
            team = re.findall(pattern, event_description)
            # if team is in team vector return else None
            return team[0]

        except AttributeError:
            return None
        except IndexError:
            return None
    else:
        return None


def get_player_name(number, players, team, home_team):
    """
    This function is used for the description field in the html. Given a last name and a number it return the player's
    full name and id.

    :param number: player's number
    :param players: all players with info
    :param team: team of player
    :param home_team: home team

    :return: dict with full and and id
    """
    venue = "Home" if team == home_team else "Away"

    # Get the info when we get the same number for that team
    player = [{'name': name, 'id': players[venue][name]['id'], 'last_name': players[venue][name]['last_name']}
              for name in players[venue].keys() if players[venue][name]['number'] == number]

    # Control for when the name can't be found
    if not player:
        player = [{'name': None, 'id': None, 'last_name': None}]

    return player[0]

def valid_event(event: list):
    """
    Filter out some events that don't provide meaningful information.

    The HTML PBP has 8 columns:
    ['#', 'Per', 'Str', 'Time:El', 'Event', 'Description', 'AWAY On Ice', 'HOME On Ice']

    :param event: list of stuff in pbp

    :return: boolean
    """
    return event[0] != '#' and event[4] not in ['GOFF', 'EGT', 'PGSTR', 'PGEND', 'ANTHEM']


def get_player_id(jersey: tuple, players: dict) -> str:
    """
    Basically takes a players jersey - a.k.a his team, name, and number, and gets his player ID

    :param jersey: tuple of info
    :param players:
    :return:
    """
    for _, venue in players.items():
        for _, player in venue.items():
            if (player['number'] == jersey[1] or jersey[1] == '') and \
                (player['team'] == jersey[0] or jersey[0] == '') and \
                (player['last_name'].upper() == jersey[2] or  jersey[2] == ''):
                return player['id']



    print(jersey)



    pass


def get_event_player_1(event: str, event_type: str, event_team: str, players) -> str:
    try:
        if event_type in ['GOAL', 'HIT', 'MISS', 'BLOCK', 'FAC']:
            pattern = re.compile("([A-Z\.]{0,3})\s*#\s*([0-9]{0,2})\s*([A-Z.]*)")
            res = re.findall(pattern, event)
            return get_player_id(res[0], players)
        elif event_type in ['SHOT', 'GIVE', 'TAKE']:
            replace = re.compile('ONGOAL\s*-\s*|GIVEAWAY\s*-\s*|TAKEAWAY\s*-\s*')
            event = re.sub(replace, '', event)
            pattern = re.compile('([A-Z\.]{0,3})\s*#\s*([0-9]{0,2})\s*([A-Z.]*)')
            res = re.findall(pattern, event)
            return get_player_id(res[0], players)
        elif event_type == "PENL" and not "TEAM" in event:
            pattern = re.compile("([A-Z\.]{0,3})\s*#\s*([0-9]{0,2})\s*([A-Z.]*)")
            res = re.findall(pattern, event)
            return get_player_id(res[0], players)
        elif event_type == "PENL" and "TEAM" in event and re.search('#[0-9]+', event):
            return event_team + re.findall('#[0-9]+', event)[0]
    except Exception:
        return None

    return None

def get_event_player_2(event: str, event_type: str, players) -> str:
    try:
        if event_type in ['BLOCK', 'FAC', 'HIT', 'PENL'] and re.search('#[0-9]+', event):
            pattern = re.compile('([A-Z\.]{0,3})\s*#\s*([0-9]{0,2})\s*([A-Z.]*)')
            res = re.findall(pattern, event)
            return get_player_id(res[1], players)
        elif event_type == 'GOAL':
            pattern = re.compile("([A-Z\.]{0,3})\s*#\s*([0-9]{0,2})\s*([A-Z.]*)")
            res = re.findall(pattern, event)
            return get_player_id(res[1], players)
    except Exception:
        return None

    return None

def get_event_player_3(event: str, event_type: str, players) -> str:
    try:
        if event_type == 'GOAL':
            pattern = re.compile("([A-Z\.]{0,3})\s*#\s*([0-9]{0,2})\s*([A-Z.]*)")
            res = re.findall(pattern, event)
            return get_player_id(res[2], players)
    except Exception:
        return None

    return None

def get_zone(event: str):
    try:
        pattern = re.compile("[a-zA-Z]{3}\.\s*[zZ]one")
        zone = re.findall(pattern, event)
        # check to see if zone is valid
        return zone[0]
    except AttributeError:
        return None
    except IndexError:
        return None


def parse_name(info):
    s = info.index('-')  # Find first hyphen
    return info[s + 1:].strip(' ')  # The name should be after the first hyphen