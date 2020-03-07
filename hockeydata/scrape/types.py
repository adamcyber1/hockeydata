"""
Data models
"""

import logging
from dataclasses import dataclass

logger = logging.getLogger('LOG.scrape')

@dataclass
class ID:
    id: int

    def __init__(self, id):
        try:
            if isinstance(id, str):
                self.id = int(id)
            elif isinstance(id, int):
                self.id = id
            else:
                msg = "ID given invalid type: {}".format(id)
                logger.error(msg)
                raise TypeError(msg)
        except Exception as e:
            msg = "ID given invalid type: {}. Error: {}".format(id, str(e))
            logger.error(msg)
            raise TypeError(msg)

    def __str__(self):
        return str(self.id)


@dataclass
class PlayerID(ID):
    def __init__(self, id):
        super().__init__(id)

@dataclass
class GameID(ID):
    id: int

    def __init__(self, id):
        super().__init__(id)

@dataclass
class Season(ID):
    id: int

    def __init__(self, id):
        super().__init__(id)