"""
The prettiest way I know how to display dataframes
"""
import tabulate


def dumps(plays, **kwargs):
    return tabulate.tabulate(plays, headers='keys', tablefmt='psql', **kwargs)


def dump(plays, fobj):
    fobj.write(dumps(plays))