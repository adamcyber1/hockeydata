import re
import importlib

from click import BadParameter, echo, UsageError, Abort
from enum import Enum
from pandas import DataFrame



def check_season(ctx, param, value: str):
    match = re.match(r"^\d{4}$|^\d{8}$|^\d{4}-\d{4}$")
    if match is None:
        raise BadParameter("Error: Season must be in the format 2016, 20162017, or 2016-2017. Input: {}".format(value))


def check_date(ctx, param, value: str):
    match = re.match(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", value)

    if match is None:
        raise BadParameter("Error: Date must be in the format YYYY-MM-DD. Input: {}".format(value))

    return value


class OutputFormat(Enum):
    TEXT = "text"
    CSV = "csv"
    JSON = "json"
    PRETTY = "pretty"

    @staticmethod
    def options():
        return list(out.value for out in OutputFormat)

    @classmethod
    def from_click_option(cls, ctx, param, value):
        try:
            return cls(value)
        except:
            raise BadParameter(value)

    def echo(self, events: DataFrame) -> None:
        try:
            formatter = importlib.import_module(
                ".output.{}".format(self.value),
                package='hockeydata'
            )
            echo(formatter.dumps(events))
        except ImportError:
            raise UsageError(
                "Output format {} is not implemented.".format(self.value)
            )
        except Exception as e:
            raise Abort(str(e))