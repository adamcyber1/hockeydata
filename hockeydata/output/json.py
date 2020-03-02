import json as _json
from pandas import DataFrame


def dump(plays, fobj):
    fobj.write(dumps(plays))

def dumps(plays: DataFrame):
    return plays.to_json(orient='records')