"""
Functions to parse the HTML roster
"""
import re

from bs4 import BeautifulSoup
from hockeydata.constants import HTMLREPORTS
import hockeydata.scrape.common as common


def get_roster(game_id: str) -> dict:
    """

    :param game_id:
    :return: dict of players and coaches
    """
    roster_html = get_raw_html(game_id)
    players, coaches = parse_html(roster_html)

    return {'players': players, 'coaches': coaches}


def get_raw_html(game_id: str):
    """
    Gets the raw Roster HTML from htmlreports.

    :param game_id:
    :return:
    """
    url = HTMLREPORTS + '{}{}/RO{}.HTM'.format(game_id[:4], int(game_id[:4]) + 1, game_id[4:])
    res = common.get_page(url)

    assert res is not None
    return res


def parse_html(html) -> tuple:
    """
    Uses bs4 to parse the raw HTML. Tries 3 different parsers.

    :param html: raw pbp
    :return: tuple: (players, head_coaches)
    """
    soup = BeautifulSoup(html, "lxml")
    players = get_players(soup)
    head_coaches = get_coaches(soup)

    if len(players) == 0:
        soup = BeautifulSoup(html.text, "html.parser")
        players = get_players(soup)
        head_coaches = get_coaches(soup)

        if len(players) == 0:
            soup = BeautifulSoup(html.text, "html5lib")
            players = get_players(soup)
            head_coaches = get_coaches(soup)

    return players, head_coaches


def remove_captaincy(player: list):
    """
    Gets rid of (A) or (C)

    :param player:

    :return:
    """
    player = re.sub('\(A\)|\(C\)', '', player[2])

    return player


def get_players(soup: BeautifulSoup) -> dict:
    tables = soup.findAll('table', {'align': 'center', 'border': '0', 'cellpadding': '0', 'cellspacing': '0', 'width': '100%'})

    # If it picks up nothing just return the empty list
    if not tables:
        return None

    del tables[0]
    player_info = [table.find_all('td') for table in tables]

    player_info = [[x.get_text() for x in group] for group in player_info]
    player_info = [[group[i:i+3] for i in range(0, len(group), 3)] for group in player_info]
    player_info = [[player for player in group if player[0] != '#'] for group in player_info]

    # Add whether the player was a scratch
    for i in range(len(player_info)):
        for j in range(len(player_info[i])):
            if i == 2 or i == 3:
                player_info[i][j].append(True)
            else:
                player_info[i][j].append(False)

    players = {'Away': player_info[0], 'Home': player_info[1]}

    # Scratches aren't always included
    if len(player_info) == 4:
        players['Away'] += player_info[2]
        players['Home'] += player_info[3]

    # First condition is to control when we get whitespace as one of the indices
    players['Away'] = [remove_captaincy(i) if i[0] != u'\xa0' else i for i in players['Away']]
    players['Home'] = [remove_captaincy(i) if i[0] != u'\xa0' else i for i in players['Home']]

    # Filter out whitespace
    players['Away'] = [i for i in players['Away'] if i[0] != u'\xa0']
    players['Home'] = [i for i in players['Home'] if i[0] != u'\xa0']

    return players

def get_coaches(soup: BeautifulSoup) -> dict:

    coaches = soup.find_all('tr', {'id': "HeadCoaches"})

    # If it picks up nothing just return the empty list
    if not coaches:
        return coaches

    coaches = coaches[0].find_all('td')

    return {
        'Away': coaches[1].get_text(),
        'Home': coaches[3].get_text()
    }