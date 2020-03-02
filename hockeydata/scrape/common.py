"""
Functions that are used by several scraping modules.
"""

import time
import datetime
import logging

from requests import Response, get, exceptions

from hockeydata.constants import NAMES, TEAMS

logger = logging.getLogger('LOG.common')

def get_page(url: str) -> Response:
    response = None
    try:
        response = get(url,timeout=5)
        response.raise_for_status()
    except exceptions.HTTPError as errh:
        logger.error("Http Error: {}".format(errh))
    except exceptions.ConnectionError as errc:
        logger.error("Error Connecting: ".format(errc))
    except exceptions.Timeout as errt:
        logger.error("Timeout Error: ".format(errt))
    except exceptions.RequestException as err:
        logger.error("Error: ".format(err))

    if response:
        return response.text

def to_seconds(minutes: str):
    if minutes == '-16:0-':
        return '1200'      #  special case

    try:
        x = time.strptime(minutes.strip(' '), '%M:%S')
    except ValueError:
        return None

    return datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

def fix_name(name: str):
    name = name.strip()
    return NAMES.get(name, name).upper()

def fix_team(team: str):
    return TEAMS.get(team, team).upper()

def safeget(container, *keys):
    for key in keys:
        if container is None:
            return None
        try:
            container = container[key]
        except KeyError:
            return None
        except IndexError:
            return None

    return container