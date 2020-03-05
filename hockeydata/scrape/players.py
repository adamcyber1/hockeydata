from hockeydata.scrape.common import fix_name, safeget
from hockeydata.scrape.html_roster import get_roster
from hockeydata.scrape.json_pbp import get_raw_json
from hockeydata.constants import TEAM_IDS_REVERSE


def get_players(game_id):
    """
    Get list of players for the game, using both HTML and JSON sources

    :param roster: players from roster html
    :param game_id: id for game

    :return: dict of players
    """
    try:
        game_json = get_raw_json(game_id)
        json_players = get_players_json(game_json['gameData']['players'])
        html_roster = get_roster(game_id)
        players = combine_players_lists(json_players, html_roster['players'])
    except Exception as e:
        return None

    return players


def get_players_json(players_json: dict) -> dict:
    """
    Return dict of players for that game

    :param players_json: players section of json

    :return: dict of players->keys are the name (in uppercase)
    """
    players = dict()

    for ID_KEY, player in players_json.items():
        players[player['fullName'].upper()] = {
                                        'id': player['id'],
                                       'first_name': player['firstName'],
                                        'last_name': player['lastName'],
                                       'number': player['primaryNumber'],
                                        'team': TEAM_IDS_REVERSE.get(player['currentTeam']['id'])
                                        }


    return players

def combine_players_lists(json_players, roster_players):
    """
    Combine the json list of players (which contains id's) with the list in the roster html

    :param json_players: dict of players w/ ids
    :param roster_players: dict of home+away players

    :return:
    """
    players = {'Home': dict(), 'Away': dict()}

    for venue in players.keys():
        for player in roster_players[venue]:
            try:
                name = fix_name(player)
                player_id = json_players[name]['id']
                players[venue][name] = {'id': player_id, 'number': json_players[name]['number'], 'last_name': json_players[name]['last_name'].upper(), 'team': json_players[name]['team']}
            except KeyError:
                continue

    return players